from Recetas import app
from flask import render_template, request, redirect, session
from Recetas.modelo.modulo_usuario import Usuarios
from flask import flash
from flask_bcrypt import Bcrypt

from Recetas.modelo.modulo_recetas import Recetas        
bcrypt = Bcrypt(app)# estamos creando un objeto llamado bcrypt
                    # que se realiza invocando la función Bcrypt con nuestra aplicación como argumento

@app.route('/')# El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def usuario():
    return render_template("registro_usuario.html")

@app.route('/registrar', methods = ['POST'])
def registrar():
    if not Usuarios.validar_usuario(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'password': pw_hash
    }
    resultado = Usuarios.crear_usuarios(data)
    return redirect('/')

@app.route('/login', methods = ['POST'])
def login():
    resultado = Usuarios.datos_usuario(request.form)
    if bcrypt.check_password_hash(resultado['password'], request.form['password']):
        session['id']  = resultado['id']
        session['nombre'] = resultado['nombre']
        session['email'] = resultado['email']
        return redirect('/recetas')
    else:
        flash("DATOS INCORRECTOS")
        return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "ESTA RUTA NO FUE ENCONTRADA", 404
    #return render_template('404.html'), 404