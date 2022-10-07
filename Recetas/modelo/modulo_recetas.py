from Recetas.configuracion.mysqlconnection import connectToMySQL
from flask import flash

# modelar la clase después de la tabla friend de nuestra base de datos
class Recetas:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre_receta = data['nombre_receta']
        self.descripcion = data['descripcion']
        self.instrucciones = data['instrucciones']
        self.tiempo = data['tiempo']
        self.fecha_creacion_receta = data['fecha_creacion_receta']
        self.creado_en = data['creado_en']
        self.actualizado_en = data['actualizado_en']

    #Validación de informacion
    @staticmethod
    def validar_receta(receta):
        print(receta)
        is_valid = True # asumimos que esto es true
        if len(receta['nombre_receta']) < 3:
            flash("NOMBRE DE RECETA DEBE TENER AL MENOS 3 CARACTERES")
            is_valid = False
        if len(receta['descripcion']) < 3:
            flash("DEBE TENER DESCRIPCCIÓN")
            is_valid = False
        if len(receta['instrucciones']) <  3:
            flash("DEBE TENER INSTRUCCIONES")
            is_valid = False
        if not(receta['fecha_creacion_receta']):
            flash("INGRESAR FECHA DE RECETA")
            is_valid = False
        if not(receta['tiempo']):
            flash("DEBE SELECCIONAR UNA OPCIÓN")
            is_valid = False
        return is_valid

    @classmethod
    def crear_recetas(cls, data):
        query = ('INSERT INTO Recetas (nombre_receta, descripcion, instrucciones, tiempo, fecha_creacion_receta, usuario_id) '
                'VALUES (%(nombre_receta)s, %(descripcion)s, %(instrucciones)s, %(tiempo)s, %(fecha_creacion_receta)s, %(usuario_id)s);')
        resultado = connectToMySQL('Recetas').query_db(query, data)
        return resultado

    @classmethod
    def todas_recetas(cls, data):
        query = "SELECT * FROM recetas join usuarios where recetas.usuario_id = usuarios.id"
        resultado = connectToMySQL('Recetas').query_db(query, data)
        return resultado

    @classmethod
    def recetas_usuario(cls, data):
        query = "SELECT * FROM recetas where usuario_id = %(id)s"
        resultado = connectToMySQL('Recetas').query_db(query, data)
        return resultado

    @classmethod
    def detalle_receta(cls, data):
        query = "SELECT * FROM recetas join usuarios where recetas.id = %(id)s"
        resultado = connectToMySQL('Recetas').query_db(query, data)
        return resultado[0]

    @classmethod
    def actualizar_recetas(cls, data):
        query = ('UPDATE recetas set nombre_receta = %(nombre_receta)s, descripcion = %(descripcion)s, instrucciones = %(instrucciones)s,'
                    'fecha_creacion_receta = %(fecha_creacion_receta)s, tiempo = %(tiempo)s '
                    'WHERE id = %(id)s;')
        resultado = connectToMySQL('Recetas'). query_db(query, data)
        return resultado

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recetas where recetas.id = %(id)s"
        resultado = connectToMySQL('Recetas').query_db(query, data)
        return resultado
