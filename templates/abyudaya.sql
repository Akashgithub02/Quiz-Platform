-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 09, 2024 at 09:02 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `abyudaya`
--

-- --------------------------------------------------------

--
-- Table structure for table `scores`
--

CREATE TABLE `scores` (
  `id` int(11) NOT NULL,
  `team_name` varchar(50) NOT NULL,
  `responses` varchar(1000) NOT NULL,
  `score` int(11) NOT NULL,
  `transaction_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `scores`
--

INSERT INTO `scores` (`id`, `team_name`, `responses`, `score`, `transaction_time`) VALUES
(31, 'team1', '{}', 0, '2024-04-09 05:55:10'),
(32, 'team1', '{}', 0, '2024-04-09 05:58:36'),
(33, 'team2', '{}', 0, '2024-04-09 06:00:22'),
(34, 'team2', '{}', 0, '2024-04-09 06:06:22'),
(35, 'team2', '{}', 0, '2024-04-09 06:19:14'),
(36, 'team2', '{}', 0, '2024-04-09 06:22:03'),
(37, 'team2', '{}', 0, '2024-04-09 06:22:17'),
(38, 'team1', '{}', 0, '2024-04-09 06:22:38'),
(39, 'team2', '{}', 0, '2024-04-09 06:24:02'),
(40, 'team2', '{}', 0, '2024-04-09 06:25:56'),
(41, 'team2', '{}', 0, '2024-04-09 06:26:01'),
(42, 'team2', '{\"0\": \"Hyper Text Markup Language\", \"1\": \"Java\", \"2\": \"Computer Style Sheets\", \"3\": \"4\", \"4\": \"Tree\", \"5\": \"Python\", \"6\": \"0 1 2 3 4\", \"7\": \"Imperative\", \"8\": \"10\", \"9\": \"Insertion Sort\", \"10\": \"Structured Question Language\", \"11\": \"HelloHelloHello\", \"12\": \"Clause\", \"13\": \"2\", \"14\": \"Angular\", \"15\": \"True\", \"16\": \"Java\", \"17\": \"2\", \"18\": \"Java\", \"19\": \"str\"}', 6, '2024-04-09 06:27:52'),
(43, 'team2', '{\"0\": \"Hyper Text Markup Language\", \"1\": \"Java\", \"2\": \"Computer Style Sheets\", \"3\": \"4\", \"4\": \"Tree\", \"5\": \"Python\", \"6\": \"0 1 2 3 4\", \"7\": \"Imperative\", \"8\": \"10\", \"9\": \"Insertion Sort\", \"10\": \"Structured Question Language\", \"11\": \"HelloHelloHello\", \"12\": \"Clause\", \"13\": \"2\", \"14\": \"Angular\", \"15\": \"True\", \"16\": \"Java\", \"17\": \"2\", \"18\": \"Java\", \"19\": \"int\"}', 5, '2024-04-09 06:28:12');

-- --------------------------------------------------------

--
-- Table structure for table `teams`
--

CREATE TABLE `teams` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `teams`
--

INSERT INTO `teams` (`id`, `name`, `password`) VALUES
(1, 'team1', 'team1'),
(2, 'team2', 'team2'),
(3, 'team3', 'team3');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `scores`
--
ALTER TABLE `scores`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `scores`
--
ALTER TABLE `scores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
