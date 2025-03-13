CREATE TABLE etl_data (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255),
    categoria VARCHAR(50),
    decada INT,
    puntuacion_ajustada FLOAT
);
