-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 28, 2017 at 07:46 AM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `solovideojuegos`
--

-- --------------------------------------------------------

--
-- Table structure for table `solovideojuegos`
--

CREATE TABLE `solovideojuegos` (
  `id_producto` int(11) NOT NULL,
  `titulo` varchar(30) NOT NULL,
  `precio` varchar(40) NOT NULL,
  `Tienda` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `solovideojuegos`
--

INSERT INTO `solovideojuegos` (`id_producto`, `titulo`, `precio`, `Tienda`) VALUES
(31, 'Danganronpa AE: Ultra Despair ', '24.990\r\n	', 'ZMART'),
(32, 'Little Nightmares: Six Edition', '34.990\r\n	', 'ZMART'),
(33, 'Guardians of the Galaxy: The T', '24.990\r\n	', 'ZMART'),
(34, 'Deformers PS4', '24.990\r\n	', 'ZMART'),
(35, 'ATV Renegades PS4', '27.990\r\n	', 'ZMART'),
(36, 'Prey PS4', '44.990\r\n	', 'ZMART'),
(37, 'Birthdays the Beginning Limite', '49.990\r\n	', 'ZMART'),
(38, 'Birthdays the Beginning PS4', '34.990\r\n	', 'ZMART'),
(39, 'Baila Latino PS4', '24.990\r\n	', 'ZMART'),
(40, 'Injustice 2 PS4', '44.990\r\n	', 'ZMART'),
(41, 'Akiba\'s Beat PS4', '39.990\r\n	', 'ZMART'),
(42, 'The Surge PS4', '44.990\r\n	', 'ZMART'),
(43, 'PSVR Farpoint PS4', '44.990\r\n	', 'ZMART'),
(44, 'Utawarerumono: Mask of Decepti', '39.990\r\n	', 'ZMART'),
(45, 'Portal Knights: Gold Throne Ed', '24.990\r\n	', 'ZMART'),
(46, 'Samurai Warriors: Spirit of Sa', '39.990\r\n	', 'ZMART'),
(47, 'Rime PS4', '27.990\r\n	', 'ZMART'),
(48, 'Tekken 7 PS4', '44.990\r\n	', 'ZMART'),
(49, 'The Elder Scrolls Online: Morr', '44.990\r\n	', 'ZMART'),
(50, 'Star Trek: Bridge Crew VR PS4', '44.990\r\n	', 'ZMART'),
(51, 'Cladun Returns: This is Sengok', '34.990\r\n	', 'ZMART'),
(52, 'Superbeat: XONiC PS4', '34.990\r\n	', 'ZMART'),
(53, 'Dirt 4 PS4', '44.990\r\n	', 'ZMART'),
(54, 'Dark Rose Valkyrie PS4', '44.990\r\n	', 'ZMART'),
(55, 'Cars 3: Driven to Win PS4', '44.990\r\n	', 'ZMART'),
(56, 'God Wars Future Past PS4', '39.990\r\n	', 'ZMART'),
(57, 'Final Fantasy XIV Online Compl', '44.990\r\n	', 'ZMART'),
(58, 'MXGP 3: The Official Motocross', '39.990\r\n	', 'ZMART'),
(59, 'Final Fantasy XIV: Stormblood ', '34.990\r\n	', 'ZMART'),
(60, 'Darksiders Warmastered Edition', '24.990\r\n	', 'ZMART');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `solovideojuegos`
--
ALTER TABLE `solovideojuegos`
  ADD PRIMARY KEY (`id_producto`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `solovideojuegos`
--
ALTER TABLE `solovideojuegos`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
