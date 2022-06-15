DROP DATABASE ihc_scm;
CREATE DATABASE IF NOT EXISTS ihc_scm;
USE ihc_scm;

CREATE TABLE doctores(
    id          INT(25) auto_increment NOT NULL,
    nombre      VARCHAR(100) NOT NULL,
    apellidos   VARCHAR(255),
    consultorio INT(25) NOT NULL,
    correo      VARCHAR(255) NOT NULL,
    password    VARCHAR(255) NOT NULL,
    CONSTRAINT pk_doctores PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(correo),
    CONSTRAINT uq_consultorio UNIQUE(consultorio)
)ENGINE=InnoDb;

CREATE TABLE consultas(
    id          INT(25) auto_increment NOT NULL,
    doctor_id   INT(25) NOT NULL,
    paciente    VARCHAR(100) NOT NULL,
    apellidos   VARCHAR(255) NOT NULL,
    edad        INT(25) NOT NULL,
    telefono    VARCHAR(255) NOT NULL,
    consultorio INT(25) NOT NULL,
    problema    MEDIUMTEXT NOT NULL,
    sexo     VARCHAR(255) NOT NULL,
    fecha       DATE NOT NULL,
    CONSTRAINT pk_consultas PRIMARY KEY(id),
    CONSTRAINT fk_consultas_Doctores FOREIGN KEY(doctor_id) REFERENCES doctores(id)
)ENGINE=InnoDb;
