-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Mar 17, 2017 at 12:25 PM
-- Server version: 10.1.16-MariaDB
-- PHP Version: 7.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `warehouse`
--

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `name` varchar(20) NOT NULL,
  `contact` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `user` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`name`, `contact`, `email`, `user`, `pass`) VALUES
('test', '1212', 'kevin@gmail.com', 'admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `stocks`
--

CREATE TABLE `stocks` (
  `proid` varchar(20) NOT NULL,
  `prona` varchar(20) NOT NULL,
  `stol` varchar(20) NOT NULL,
  `disc` varchar(20) NOT NULL,
  `cpu` varchar(20) NOT NULL,
  `oi` varchar(20) NOT NULL,
  `cust` varchar(20) NOT NULL,
  `ons` varchar(20) NOT NULL,
  `ior` varchar(20) NOT NULL,
  `add` varchar(20) NOT NULL,
  `amount` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `stocks`
--

INSERT INTO `stocks` (`proid`, `prona`, `stol`, `disc`, `cpu`, `oi`, `cust`, `ons`, `ior`, `add`, `amount`) VALUES
('', '', '', '', '', '', '', '', '', '', 0),
('', '', '', '', '', '', '', '', '', '', 0),
('', '', '', '', '', '', '', '', '', '', 0),
('', '', '', '', '', '', '', '', '', '', 0),
('', '', '', '', '', '', '', '', '', '', 0),
('', '', '', '', '', '', '', '', '', '', 0),
('asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd', '123', '123', 123);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
