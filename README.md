MF0492_3

# ESTRUCTURA WEB FLASK

-----------------------------



.env
docker-compose.yml
Dockerfile
requirements.txt
readme.md
app /
    app.py
    db.py
    templates/
        form.html
db /
    init.sql
docker-entrypoint-intdb.d/
    01-init.sql (copia de db/init.sql)

------------------------


La carpeta
/docker-entrypoint-initdb.d se utiliza en imágenes de Docker de bases de datos (como MySQL, PostgreSQL, MariaDB) para ejecutar automáticamente scripts SQL o de shell (.sql, .sh) durante la primera inicialización del contenedor. Permite sembrar datos, crear tablas o usuarios automáticamente al levantar el contenedor. 
Aspectos clave:

    Ejecución única: Los archivos contenidos se ejecutan únicamente la primera vez que se crea el volumen de la base de datos.
    Orden alfabético: Los archivos se ejecutan en orden alfabético.
    Uso común: Se monta mediante volúmenes en el docker-compose.yml para inicializar la estructura de la base de datos sin entrar manualmente al contenedor.
    Archivos .sql: Se importan alfanuméricamente en la base de datos por defecto.
    Archivos .sh: Se ejecutan para realizar configuraciones previas personalizadas. 

Es una práctica estándar para asegurar que la base de datos esté lista con los datos necesarios al iniciar el entorno.


REPO. POSTGRES BD DOCKER.

https://hub.docker.com/_/postgres/

REPO. DOCKER. BD EJEMPLO.

https://github.com/jorgepacheco/docker_for_bbdd/tree/master/example-postgres