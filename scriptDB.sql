CREATE DATABASE BearCareful;
USE BearCareful;

CREATE TABLE CPais(

    id_pais INT NOT NULl AUTO_INCREMENT,
    nom_pais VARCHAR(20) NOT NULL,
    PRIMARY KEY(id_pais)

);

CREATE TABLE MUsuario(

    id_usu INT NOT NULl AUTO_INCREMENT,
    id_pais INT NOT NULL,
    nom_usu VARCHAR(20) NOT NULL,
    con_usu VARCHAR(20) NOT NULL,
    cor_usu VARCHAR(32) NOT NULL,
    PRIMARY KEY(id_usu),
    FOREIGN KEY(id_pais) REFERENCES CPais(id_pais)
);

CREATE TABLE MRegistro(

    id_reg INT NOT NULL AUTO_INCREMENT,
    id_pais INT NOT NULL,
    ind DECIMAL NOT NULL,
    year INT NOT NULL,
    PRIMARY KEY(id_reg),
    FOREIGN KEY(id_pais) REFERENCES CPais(id_pais)

);

CREATE TABLE CEscala(

    id_esc INT NOT NULL AUTO_INCREMENT,
    esc VARCHAR(20) NOT NULL,
    PRIMARY KEY(id_esc)
);

CREATE TABLE MTEST(

    id_test INT NOT NULL AUTO_INCREMENT,
    id_usu INT NOT NULL,
    id_esc INT NOT NULL,
    fec DATE NOT NULL,
    res INT NOT NULL,
    PRIMARY KEY(id_test),
    FOREIGN KEY(id_usu) REFERENCES MUsuario(id_usu),
    FOREIGN KEY(id_esc) REFERENCES CEscala(id_esc)

);

CREATE TABLE GRAFICA(
    historico
    id_usu
    codigo
)

INSERT INTO cpais (nom_pais)
VALUES ('CAN'); -- id 1

INSERT INTO cpais (nom_pais)
VALUES ('USA'); -- id 2

INSERT INTO cpais (nom_pais)
VALUES ('MEX'); -- id 3

INSERT INTO musuario (id_pais, nom_usu, con_usu, cor_usu)
VALUES (1, 'Luis', 'pillofon', 'luis@luis.com'); -- id 1

INSERT INTO musuario (id_pais, nom_usu, con_usu, cor_usu)
VALUES (2, 'Edgar', 'marin', 'marin@s.com'); -- id 2

INSERT INTO musuario (id_pais, nom_usu, con_usu, cor_usu)
VALUES (3, 'Alexis', 'oso', 'oso@s.com'); -- id 3

INSERT INTO cescala (esc)
VALUES ('Bien'); -- id 1

INSERT INTO cescala (esc)
VALUES ('Maso'); -- id 2

INSERT INTO cescala (esc)
VALUES ('Mal'); -- id 3

INSERT INTO cescala (esc)
VALUES ('Muriendo'); -- id 4

INSERT INTO mtest (id_usu, id_esc, fec, res)
VALUES (1, 4, '2021-01-01', 25); -- id 1

INSERT INTO mtest (id_usu, id_esc, fec, res)
VALUES (1, 4, '2021-01-15', 21); -- id 2

INSERT INTO mtest (id_usu, id_esc, fec, res)
VALUES (1, 3, '2021-02-01', 17); -- id 3

--Esta no
INSERT INTO mtest (id_usu, id_esc, fec, res)
VALUES (1, 2, '2021-01-01', 12); -- id 4
--

INSERT INTO mtest (id_usu, id_esc, fec, res)
VALUES (2, 2, '2021-01-01', 12); -- id 5

INSERT INTO mtest (id_usu, id_esc, fec, res)
VALUES (1, 2, '2021-02-18', 12); -- id 6

INSERT INTO mtest (id_usu, id_esc, fec, res)
VALUES (1, 1, '2021-03-10', 10);

INSERT INTO mtest (id_usu, id_esc, fec, res)
VALUES (1, 2, '2021-03-28', 12);

INSERT INTO mtest (id_usu, id_esc, fec, res)
VALUES (1, 1, '2021-04-10', 10);

INSERT INTO mtest (id_usu, id_esc, fec, res)
VALUES (1, 2, '2021-04-28', 12);

SELECT fec, res FROM mtest WHERE id_usu=1;

DELETE FROM mtest WHERE id_test= 4;