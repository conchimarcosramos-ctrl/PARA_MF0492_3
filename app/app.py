from flask import Flask, render_template, request, redirect
from db import get_all_pedidos, insert_pedido
from datetime import datetime

app = Flask(__name__)

#route en flask se utiliza para definir la ruta de una página web, 
#asociando caminos específicos a funciones que se ejecutarán cuando 
#se acceda a esas rutas. 
#En este caso, la ruta '/' se asocia con la función index(), 
#que se encargará de mostrar el formulario para crear un nuevo pedido 
#y la lista de pedidos existentes. La ruta '/create' se asocia con la función add_pedido(), que se encargará de procesar los datos enviados desde el formulario para crear un nuevo pedido en la base de datos.

#app.route nos da el contenido a mostrar en la página principal, 
#en este caso el formulario para crear un nuevo pedido y la lista de pedidos existentes.
@app.route('/')
def index():
    pedidos = get_all_pedidos()  #obtenemos todos los pedidos de la base de datos
    return render_template('form.html', pedidos=pedidos)  #renderizamos la plantilla form.html y le pasamos los pedidos obtenido

#app.route en add_pedido se encarga de procesar los datos enviados desde el formulario 
#para crear un nuevo pedido en la base de datos.
@app.route('/create', methods=['POST'])
def add_pedido():
    nome_cliente = request.form['nome_cliente']  #obtenemos el nombre del cliente del formulario
    producto = request.form['producto']          #obtenemos el producto del formulario
    cantidade = request.form['cantidade']        #obtenemos la cantidad del formulario
    data_pedido = request.form ['data_pedido']   #obtenemos la fecha y hora actual para el pedido

    insert_pedido(nome_cliente, producto, cantidade, data_pedido)  #insertamos el nuevo pedido en la base de datos
    return redirect('/')  #redireccionamos a la página principal para mostrar el nuevo pedido agregado:

#if __name__ == '__main__': es una construcción común en Python que se utiliza para 
#asegurarse de que el código dentro de este bloque solo se ejecute cuando el script 
#se ejecute directamente, y no cuando se importe como un módulo en otro script. 
#En este caso, se utiliza para ejecutar la aplicación Flask solo si el script se 
#ejecuta directamente, lo que es útil para evitar que la aplicación se ejecute
#accidentalmente si el archivo es importado por otro módulo.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)  
    
    #con app.run ejecutamos la aplicación en modo debug para facilitar el desarrollo 
    #y la depuración de errores
    