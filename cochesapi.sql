-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-03-2023 a las 18:49:08
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `cochesapi`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `coches`
--

CREATE TABLE `coches` (
  `id` int(255) NOT NULL,
  `modelo` varchar(1000) NOT NULL,
  `año` int(255) NOT NULL,
  `bastidor` int(255) NOT NULL,
  `titular` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `coches`
--

INSERT INTO `coches` (`id`, `modelo`, `año`, `bastidor`, `titular`) VALUES
(1, 'MX-5', 2009, 1232, 'Aleksandr Lilie'),
(3, 'Expedition', 2002, 1234, 'Maurene Erik'),
(4, 'Stratus', 2000, 0, 'Raf Quilty'),
(5, 'MX-5', 1996, 2, 'Rod McVitie'),
(6, '940', 1994, 0, 'Lucille Enevold'),
(8, 'nuevo', 0, 0, 'YO'),
(9, 'S80', 1999, 3, 'Dorothea Inch'),
(10, 'Kizashi', 2011, 1, 'Nuevo titular ACTUALIZADO ¡pero solo el titular!'),
(11, 'S5', 2012, 0, 'Tommi Domnick'),
(12, 'GTO', 1997, 1, 'Josefina McReidy'),
(13, 'Prius', 2004, 3, 'Carolynn Fidge'),
(14, 'Blazer', 2001, 0, 'Iolande Stayte'),
(15, 'CX-7', 2009, 1, 'Karissa Dudill'),
(16, 'GT500', 2007, 0, 'Christos Beggi'),
(17, 'MR2', 1995, 0, 'Fania Cochet'),
(18, 'Grand Prix', 1962, 1, 'Kessiah Fursse'),
(19, 'Malibu', 2001, 0, 'Lyda Spoors'),
(20, 'Colorado', 2011, 1, 'Dreddy Mainds'),
(22, 'BMW', 2023, 1234567, 'El Rafa'),
(24, 'BMW', 2023, 1234567, 'El Davas'),
(25, 'BMW', 2023, 1234567, 'El Rafa'),
(27, 'Pajero', 1980, 2147483647, 'Rafa'),
(45, 'sgh', 2002, 1234, 'dffsh'),
(47, 'Nuevo coche ACTUALIZADO', 2023, 1234, 'Nuevo titular ACTUALIZADO'),
(96, '1234', 1980, 765432, 'El Rafa'),
(97, '1234', 1980, 765432, 'H'),
(98, '1234', 1980, 765432, 'El Rafa'),
(99, '1234', 1980, 765432, 'El Rafa'),
(123, '123', 123, 123, 'Rafa'),
(124, 'aa', 0, 0, 'El aa'),
(125, 'b', 0, 0, 'El b'),
(123456789, '1234567890', 123456789, 123456789, 'El 123456789');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `coches`
--
ALTER TABLE `coches`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `coches`
--
ALTER TABLE `coches`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=123456790;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
