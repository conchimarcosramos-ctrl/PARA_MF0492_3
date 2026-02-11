FROM python:3.12-slim
#indicamos que la imagen base es python 3.12 en su versión slim, lo que significa que es una imagen ligera de Python.

WORKDIR /app
#indicamos que la carpeta de trabajo es /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#copiamos el archivo requirements.txt a la carpeta de trabajo y 
#luego instalamos las dependencias listadas en ese archivo utilizando pip.

COPY app/ .
#copiamos el contenido de la carpeta app a la carpeta de trabajo.

EXPOSE 8000
#exponemos el puerto 8000.

CMD ["python", "app.py"]
#indicamos el comando que se ejecutará cuando se inicie el contenedor, 
#en este caso, se ejecutará el archivo app.py utilizando Python.
