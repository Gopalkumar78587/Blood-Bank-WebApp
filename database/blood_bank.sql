-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 08, 2023 at 08:03 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `blood_bank`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `key` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`, `key`) VALUES
('admin', 'admin', 'xyz123');

-- --------------------------------------------------------

--
-- Table structure for table `bb_donor`
--

CREATE TABLE `bb_donor` (
  `id` int(11) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `dob` varchar(15) NOT NULL,
  `address` varchar(50) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `city` varchar(20) NOT NULL,
  `blood_grp` varchar(20) NOT NULL,
  `donor` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bb_donor`
--

INSERT INTO `bb_donor` (`id`, `uname`, `name`, `gender`, `dob`, `address`, `mobile`, `email`, `city`, `blood_grp`, `donor`, `pass`) VALUES
(1, 'BBH1', 'Siva', 'Male', '1999-12-12', 'DD Nagar', 8977495254, 'siva11@gmail.com', 'Trichy', 'A+ve', 'BD1', '1234'),
(2, 'BBH1', 'Rahul', 'Male', '1995-03-02', '44, KJ Nagar', 8879956143, 'rahul@gmail.com', 'Thanjavur', 'O+ve', 'BD2', '1234'),
(3, 'BBH2', 'Rekha', 'Female', '1991-04-04', 'RR Nagar', 8875644985, 'rekha@gmail.com', 'Madurai', 'B+ve', 'BD3', '1234'),
(4, 'BBH2', 'Sankar', 'Male', '1993-06-05', 'FF Nagar', 8895477147, 'sankar@gmail.com', 'Madurai', 'A-ve', 'BD4', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `bb_register`
--

CREATE TABLE `bb_register` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `location` varchar(30) NOT NULL,
  `city` varchar(30) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL,
  `utype` varchar(20) NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bb_register`
--

INSERT INTO `bb_register` (`id`, `name`, `mobile`, `email`, `location`, `city`, `uname`, `pass`, `utype`, `status`) VALUES
(1, 'Apollo', 9985424163, 'apollo@gmail.com', '55, TN Nagar', 'Trichy', 'BBH1', '123456', 'Blood Bank', 1),
(2, 'Krishna', 7758944158, 'krishna@gmail.com', '44, MK Road,', 'Madurai', 'BBH2', '123456', 'Blood Bank', 1);

-- --------------------------------------------------------

--
-- Table structure for table `bb_send`
--

CREATE TABLE `bb_send` (
  `id` int(11) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `message` varchar(100) NOT NULL,
  `etime` varchar(20) NOT NULL,
  `blood_grp` varchar(10) NOT NULL,
  `rdate` varchar(15) NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bb_send`
--

INSERT INTO `bb_send` (`id`, `uname`, `message`, `etime`, `blood_grp`, `rdate`, `status`) VALUES
(1, 'BBH1', 'required', 'tomorrow 3pm', 'A+ve', '08-03-2023', 0);

-- --------------------------------------------------------

--
-- Table structure for table `bb_send_donor`
--

CREATE TABLE `bb_send_donor` (
  `id` int(11) NOT NULL,
  `sid` int(11) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `donor` varchar(20) NOT NULL,
  `blood_grp` varchar(10) NOT NULL,
  `status` int(11) NOT NULL,
  `rdate` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bb_send_donor`
--

INSERT INTO `bb_send_donor` (`id`, `sid`, `uname`, `donor`, `blood_grp`, `status`, `rdate`) VALUES
(1, 1, 'BBH1', 'BD1', 'A+ve', 3, '08-03-2023');
