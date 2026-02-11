CREATE DATABASE pedidos_db;

-- Conectar la base de datos creada -- 
-- es un comando psql que significa "conectar a la base de datos pedidos_db" --
-- cambia la conexión actual a la base de datos pedidos_db para ejecutar comandos -- 
-- QL en esa base de datos --

\c pedidos_db;
CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    nome_cliente VARCHAR(255) NOT NULL,
    producto VARCHAR(255) NOT NULL,
    cantidade INT NOT NULL,
    data_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);