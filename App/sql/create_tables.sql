DROP TABLE IF EXISTS tabla_general;
CREATE TABLE tabla_general
(
    id_tabla_general serial NOT NULL,
    cod_localidad integer,
    id_provincia integer,
    id_departamento integer,
    categoria VARCHAR(255),
    provincia VARCHAR(255),
    localidad VARCHAR(255),
    nombre VARCHAR(255),
    domicilio VARCHAR(255),
    codigo_postal VARCHAR(255),
    numero_de_telefono VARCHAR(255),
    mail VARCHAR(255),
    web VARCHAR(255),
    fecha_de_carga date,
    PRIMARY KEY (id_tabla_general)
);

DROP TABLE IF EXISTS cant_categoria;
CREATE TABLE cant_categoria
(
    id_cant_categoria serial NOT NULL,
    categoria VARCHAR(255),
    cantidad integer,
    fecha_de_carga date,
    PRIMARY KEY (id_cant_categoria)
);

DROP TABLE IF EXISTS cant_fuente;
CREATE TABLE cant_fuente
(
    id_cant_fuente serial NOT NULL,
    fuente VARCHAR(255),
    cantidad integer,
    fecha_de_carga date,
    PRIMARY KEY (id_cant_fuente)
);

DROP TABLE IF EXISTS cant_provincia_categoria;
CREATE TABLE cant_provincia_categoria
(
    id_cant_provincia_categoria serial NOT NULL,
    provincia VARCHAR(255),
    categoria VARCHAR(255),
    cantidad integer,
    fecha_de_carga date,
    PRIMARY KEY (id_cant_provincia_categoria)
);

DROP TABLE IF EXISTS salas_de_cine;
CREATE TABLE salas_de_cine
(
    id_salas_de_cine serial NOT NULL,
    provincia VARCHAR(255),
    cant_pantallas integer,
    cant_butacas integer,
    cant_espacios_incaa integer,
    fecha_de_carga date,
    PRIMARY KEY (id_salas_de_cine)
);