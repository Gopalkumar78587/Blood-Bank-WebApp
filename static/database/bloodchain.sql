-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 02, 2022 at 03:23 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `bloodchain`
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
-- Table structure for table `bb_bag`
--

CREATE TABLE `bb_bag` (
  `id` int(11) NOT NULL,
  `bag_id` varchar(20) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `blood_grp` varchar(20) NOT NULL,
  `donor` varchar(20) NOT NULL,
  `rdate` varchar(20) NOT NULL,
  `collected_temp` double NOT NULL,
  `temp` double NOT NULL,
  `status` int(11) NOT NULL,
  `rtime` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `tlocation` varchar(50) NOT NULL,
  `tdate` varchar(20) NOT NULL,
  `ttime` varchar(20) NOT NULL,
  `req_st` int(11) NOT NULL,
  `req_bank` varchar(20) NOT NULL,
  `dtime` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bb_bag`
--

INSERT INTO `bb_bag` (`id`, `bag_id`, `uname`, `blood_grp`, `donor`, `rdate`, `collected_temp`, `temp`, `status`, `rtime`, `name`, `tlocation`, `tdate`, `ttime`, `req_st`, `req_bank`, `dtime`) VALUES
(1, 'BB1', 'BBH2', 'A+ve', 'BD1', '01-05-2022', 0, 3, 1, '12:58:05 PM', 'Ram', 'Madurai', '02-05-2022', '06:46:30 AM', 0, '', '2022-05-02 08:25:19'),
(2, 'BB2', 'BBH2', 'A+ve', 'BD1', '01-05-2022', 0, 2, 0, '12:58:24 PM', '', '', '', '', 2, 'BBH1', '2022-05-02 08:27:14'),
(3, 'BB3', 'BBH2', 'B+ve', 'BD2', '01-05-2022', 0, 4, 0, '12:58:51 PM', '', '', '', '', 0, '', '2022-05-02 08:24:00');

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
(1, 'BBH2', 'Ram', 'Male', '1994-04-14', '57,ad st', 9054621096, 'rndittrichy@gmail.com', 'Trichy', 'A+ve', 'BD1', '1234'),
(2, 'BBH2', 'Dinesh', 'Male', '1992-04-21', '33,KS Nagar', 9054621096, 'dinesh@gmail.com', 'Salem', 'B+ve', 'BD2', '1234'),
(3, 'BBH1', 'Vinay', 'Male', '1996-05-04', '34,FF', 8807655342, 'vinay@gmail.com', 'Chennai', 'A1+ve', 'BD3', '1234');

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
(1, 'Apollo', 9956744242, 'apollo@gmail.com', 'DD Nagar', 'Chennai', 'BBH1', '1234', 'Hospital', 1),
(2, 'KMC', 9054621096, 'kmc@gmail.com', '45,AP', 'Chennai', 'BBH2', '1234', 'Hospital', 1),
(3, 'Annai Blood Centre', 9054621096, 'annai@gmail.com', '33,GH', 'Madurai', 'BBC3', '1234', 'Blood Bank', 0);

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
(1, 'BBH1', 'require', '3-5-22, 3pm', 'A1+ve', '02-05-2022', 0);

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
(1, 1, 'BBH1', '3', 'A1+ve', 1, '02-05-2022');
