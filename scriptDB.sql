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
    año INT NOT NULL,
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