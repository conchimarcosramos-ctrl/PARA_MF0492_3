import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

#dotenv lo usaremos para cargar las variables de entorno desde un archivo .env
#psycopg2-binary lo usaremos para conectar a la base de datos
#psycopg2.extras.RealDictCursor lo usaremos para obtener los resultados de las consultas en formato de diccionario, lo que facilita el acceso a los datos por nombre de columna en lugar de por índice.
#psycopg2 lo usaremos para abrir la conexión
#creamos la primera función para  obtener la variable del entorno

load_dotenv()   #cargamos las variables de entorno desde el archivo .env

#definimos la conexión con la bd
def get_db_connection():
    """Conecta a la base de datos y devuelve la conexión."""
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", 'localhost'),             #obtenemos la variable de entorno para el host, si no existe usamos 'localhost' por defecto
        database=os.getenv("DB_NAME", 'pedido_bd'),         #obtenemos la variable de entorno para el nombre de la base de datos, si no existe usamos 'pedido_bd' por defecto
        user=os.getenv("DB_USER", 'postgres'),              #obtenemos la variable de entorno para el usuario, si no existe usamos 'postgres' por defecto
        password=os.getenv("DB_PASSWORD", 'postgres'),      #obtenemos la variable de entorno para la contraseña, si no existe usamos 'postgres' por defecto    
        port=os.getenv("DB_PORT", 5432)                      #obtenemos la variable de entorno para el puerto, si no existe usamos 5432 por defecto  
    )
    return conn

def get_all_pedidos():
    """Obtiene todos los pedidos de la base de datos."""
    conn = get_db_connection()                              #obtenemos la conexion
    cursor = conn.cursor(cursor_factory=RealDictCursor)     #creamos el cursor
    cursor.execute("SELECT * FROM pedidos")                 #ejecutamos la consulta para obtener todos los pedidos
    pedidos = cursor.fetchall()                             #obtenemos todos los resultados
    cursor.close()                                          #cerramos el cursor
    conn.close()                                            #cerramos la conexión
    return pedidos                                          #devolvemos los pedidos obtenidos

def insert_pedido(nome_cliente, producto, cantidade, data_pedido=None):
    """Crea un nuevo pedido en la base de datos."""
    conn = get_db_connection()      #obtenemos la conexión
    cursor = conn.cursor()          #creamos el cursor
    cursor.execute(                         
        'INSERT INTO pedidos (nome_cliente, producto, cantidade, data_pedido) VALUES (%s, %s, %s, %s)', 
        (nome_cliente, producto, cantidade, data_pedido)
    )               #ejecutamos la consulta para insertar un nuevo pedido en la tabla pedidos
    conn.commit()   #confirmamos los cambios en la base de datos
    cursor.close()  #cerramos el cursor
    conn.close()    #cerramos la conexión
        
    
    return {"message": "Pedido creado correctamente."}  
    #devolvemos un mensaje de confirmación
