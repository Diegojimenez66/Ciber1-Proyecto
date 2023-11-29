CREATE DATABASE IF NOT EXISTS PEPS;
USE PEPS;
CREATE TABLE maquinas(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    precio DECIMAL(9,2) NOT NULL,
	foto VARCHAR(255)
);
CREATE TABLE usuarios(
	usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    clave VARCHAR(255) NOT NULL,
    perfil VARCHAR(100) NOT NULL,
    fechaUltimoAcceso DATE
);
INSERT INTO `usuarios` (`usuario`, `clave`, `perfil`, `fechaUltimoAcceso`) VALUES ('root', '1234', 'admin', '2022-03-01');
INSERT INTO `maquinas` (`nombre`, `descripcion`, `precio`, `foto`) VALUES ('Cinta de correr', 'Cinta para correr con varias velocidades', 100, 'https://www.fitnessdigital.com/images/productos/XL/17/BH-iF1Run-1.jpg');
INSERT INTO `maquinas` (`nombre`, `descripcion`, `precio`, `foto`) VALUES ('Polea', 'Para multiples ejercicios', 30, 'https://www.corpomachine.com/Files/48757/Img/17/estacion-de-poleas-ATX-maquina-de-musculacion-0001-zoom.jpg');
INSERT INTO `maquinas` (`nombre`, `descripcion`, `precio`, `foto`) VALUES ('Banca', 'Apollo para realizar ejercicios', 50, 'https://www.corpomachine.com/Files/48757/Img/06/atx-press-de-banca-profesional-con-barras-de-seguridad-0001-zoom.jpg');
INSERT INTO `maquinas` (`nombre`, `descripcion`, `precio`, `foto`) VALUES ('Mancuernas', 'Para levantar peso', 40, 'https://vioksport.es/wp-content/uploads/2018/06/Mancuernas-Hexagonales.jpg');
INSERT INTO `maquinas` (`nombre`, `descripcion`, `precio`, `foto`) VALUES ('Estación de dominadas', 'Para realizar dominadas', 150, 'https://m.media-amazon.com/images/I/41FntAAR1YL._AC_.jpg');
INSERT INTO `maquinas` (`nombre`, `descripcion`, `precio`, `foto`) VALUES ('Power rack', 'Soporte para pesos', 200, 'https://resources.sport-tiedje.com/bilder/bodycraft/f430-set/bodycraft-f430-rft-set-01_1600.jpg');