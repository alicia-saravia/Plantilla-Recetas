from Recetas.configuracion.mysqlconnection import connectToMySQL
from flask import flash
import re	# el módulo regex
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# modelar la clase después de la tabla friend de nuestra base de datos
class Usuarios:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.creado_en = data['creado_en']
        self.actualizado_en = data['actualizado_en']

    #Validación de informacion
    @staticmethod
    def validar_usuario(usuario):
        is_valid = True # asumimos que esto es true
        if len(usuario['nombre']) < 3:
            flash("NOMBRE DEBE TENER AL MENOS 3 CARACTERES")
            is_valid = False
        if len(usuario['apellido']) < 3:
            flash("APELLIDO DEBE TENER AL MENOS 3 CARACTERES")
            is_valid = False
        if not EMAIL_REGEX.match(usuario['email']): 
            flash("DIRECCIÓN DE EMAIL INCORRECTA")
            is_valid = False 
        if not usuario['password'] == usuario['confirmar_password']:
            flash("PASSWORD NO COINCIDEN")
            is_valid
        query = "SELECT * FROM usuarios where email = %(email)s;"
        resultado = connectToMySQL('Recetas').query_db(query, usuario)
        print (resultado)
        if resultado:
            flash("DIRECCIÓN DE EMAIL YA EXISTENTE")
            is_valid = False 
        return is_valid
    
    @classmethod
    def crear_usuarios(cls, data):
        query = """INSERT INTO usuarios (nombre, apellido, email, password)
                    VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);"""
        resultado = connectToMySQL('Recetas').query_db(query, data)
        return resultado

    @classmethod
    def datos_usuario(cls, data):
        query = "SELECT * FROM usuarios where email = %(email)s;"
        resultado = connectToMySQL('Recetas').query_db(query, data)
        return resultado[0]

    
