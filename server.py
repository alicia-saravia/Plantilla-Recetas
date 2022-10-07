from Recetas import app
from Recetas.controlador import controlador_usuario
from Recetas.controlador import controlador_recetas


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración