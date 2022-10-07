from Recetas import app
from flask import render_template, request, redirect, session
from Recetas.modelo.modulo_recetas import Recetas
from flask import flash
from flask_bcrypt import Bcrypt


from Recetas.modelo.modulo_recetas import Recetas        
bcrypt = Bcrypt(app)# estamos creando un objeto llamado bcrypt
                    # que se realiza invocando la función Bcrypt con nuestra aplicación como argumento

@app.route('/nueva_receta', methods = ['POST'])
def nueva_receta():
    if not session:
        return redirect('/')
    if not Recetas.validar_receta(request.form):
        return redirect('/recetas/nueva')
    resultado = Recetas.crear_recetas(request.form)
    return redirect('/recetas')

@app.route('/recetas')
def recetas():
    if not session:
        return redirect('/')
    data = {
        "id" : session["id"]
    }
    resultado = Recetas.todas_recetas(data)
    return render_template("publicacion_recetas.html", usuario = session, recetas = resultado)

@app.route('/recetas/nueva')
def recetas_nuevas():
    if not session:
        return redirect('/')
    return render_template("nueva_receta.html")

@app.route('/recetas/editar/<id>')
def editar_receta(id):
    if not session:
        return redirect('/')
    data = {
        'id': id
    }
    resultado = Recetas.detalle_receta(data)
    return render_template("actualizar_receta.html", receta = resultado)

@app.route('/recetas/<id>')
def detalle_receta(id):
    if not session:
        return redirect('/')
    data = {
        'id': id
    }
    resultado = Recetas.detalle_receta(data)
    print(resultado)
    return render_template('detalle_receta.html',receta = resultado)

@app.route('/delete/<id>')
def delete(id):
    if not session:
        return redirect('/')
    data = {
        'id': id
    }
    resultado = Recetas.delete(data)
    print(resultado)
    return redirect('/recetas')

@app.route('/actualizar_receta', methods = ['POST'])
def actualizar_receta():
    if not session:
        return redirect('/')
    if not Recetas.validar_receta(request.form):
        return redirect('/recetas/editar/'+ request.form['id'])
    resultado = Recetas.actualizar_recetas(request.form)
    return redirect('/recetas')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "ESTA RUTA NO FUE ENCONTRADA", 404
    #return render_template('404.html'), 404