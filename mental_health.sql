-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 18, 2025 at 07:55 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mental_health`
--

-- --------------------------------------------------------

--
-- Table structure for table `chat`
--

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL,
  `user_reg_id` int(11) NOT NULL,
  `question` text NOT NULL,
  `answer` text NOT NULL,
  `date_time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `chat`
--

INSERT INTO `chat` (`chat_id`, `user_reg_id`, `question`, `answer`, `date_time`) VALUES
(1, 1, 'hi', 'Hi! It\'\'s nice to meet you. Is there something I can help you with or would you like to chat?\n\nWould you like to continue talking about this or share something else?', '2025-01-18 04:45:20'),
(2, 1, 'I\'ve been feeling really down lately, like everything is just too much. I don\'t know where to turn.', 'I\'\'m so sorry to hear that you\'\'re feeling overwhelmed and struggling to know where to turn. It\'\'s completely normal to feel this way, and I\'\'m here to listen and offer some support.\n\nFirstly, please know that you\'\'re not alone in this feeling. Many people have been where you are, and it\'\'s okay to feel like everything is too much. It\'\'s a heavy burden to carry, and it\'\'s understandable that you might feel like you\'\'re drowning in it all.\n\nCan you tell me a bit more about what\'\'s been going on and how you\'\'ve been feeling? Sometimes talking about it can help clarify things and give us a sense of direction forward.\n\nIn the meantime, here are some things that might be helpful to know:\n\n1. **You don\'\'t have to face this alone**: There are people who care about you and want to help. Whether it\'\'s a friend, family member, or professional, there are resources available to support you.\n2. **It\'\'s okay to not be okay**: It\'\'s okay to admit that you\'\'re struggling and that you need help. People often put on a brave face or pretend like everything is fine when in reality, they\'\'re feeling overwhelmed.\n3. **You\'\'re not expected to have all the answers**: There\'\'s no one-size-fits-all solution, and that\'\'s okay. It\'\'s okay to not know what to do or where to turn.\n4. **Small steps can add up**: Sometimes, it\'\'s the smallest steps that can lead to the biggest changes. breaks things down into smaller, manageable chunks, and focus on making progress one step at a time.\n5. **Professional help is available**: If you\'\'re struggling to cope with your emotions, there are professionals who can help. Therapy is a confidential and supportive environment where you can talk about your feelings, gain new perspectives, and develop coping strategies.\n\nRemember, you\'\'re not a failure or weak because you\'\'re struggling. These feelings are normal, and they can pass.\n\nWhat do you think? Is there anything specific that\'\'s been on your mind lately that you\'\'d like to talk about?\n\nWould you like to continue talking about this or share something else?', '2025-01-18 04:46:22'),
(3, 1, 'Ive been feeling really down lately, like everything is just too much. I dont know where to turn.', 'Im so sorry to hear that youre feeling overwhelmed and down. Its completely normal to feel that way, especially when life feels too much to handle. It takes a lot of courage to acknowledge and share your feelings with someone. Im here to listen and offer support, if youd like to talk about whats on your mind.\n\nFirstly, please know that youre not alone in this feeling. Many people struggle with similar emotions, and its okay to not be okay. Its important to remember that your emotions are valid and normal.\n\nIf you feel comfortable, could you tell me a bit more about whats been going on and how youve been feeling? Sometimes talking about our struggles can help us feel a sense of relief and clarity. Dont worry about sharing too much - just enough to get things off your chest can be helpful.\n\nIn the meantime, here are a few resources that might be helpful:\n\n1. Crisis Hotlines:\n	* National Suicide Prevention Lifeline (1-800-273-TALK (8255) in the US)\n	* Crisis Text Line (text HOME to 741741 in the US)\n	* Your countrys emergency services or mental health crisis line\n2. Online Support:\n	* National Alliance on Mental Illness (NAMI) helpline (1-800-950-6264 in the US)\n	* Mental Health America (www.mhanational.org)\n	* Your countrys mental health organization or support groups\n3. Self-Care:\n	* Take a few minutes to do something that brings you joy, relaxation, or comfort. Whether its taking a warm bath, going for a walk, or practicing yoga, prioritize self-care.\n\nRemember, you dont have to face this alone. There are people who care and want to help. If you need someone to talk to, a listening ear, or guidance, Im here for you.\n\nWould you like to continue talking about this or share something else?', '2025-01-18 04:53:03'),
(4, 1, 'I dont think theyd understand. It’s not like I want to burden anyone with my problems.', 'I can sense the hesitation and concern you have about sharing your problems with others. Its completely normal to feel this way! Many people struggle with opening up to others about their struggles, fearing that they might be judged, rejected, or overwhelmed by our concerns.\n\nHowever, its important to remember that often, the people around us care deeply about us and want to help. They may not be burdened by your problems at all, but instead, they may find ways to support and_RESOURCE_ you.\n\nIf youre not comfortable sharing your problems with friends or family, consider reaching out to a professional therapist or counselor. They are trained to listen and provide guidance without judgment. They can help you work through your challenges and develop coping strategies to navigate difficult situations.\n\nRemember, you dont have to carry your burdens alone. Its okay to ask for help, and its okay to prioritize your own well-being. Would you like to talk more about whats been going on and how youre feeling? Im here to listen and support you.\n\nWould you like to continue talking about this or share something else?', '2025-01-18 04:56:03'),
(5, 1, 'hi', 'Hi! Its nice to meet you. Is there something I can help you with or would you like to chat?\n\nWould you like to continue talking about this or share something else?', '2025-01-18 05:08:48'),
(6, 1, 'hello', 'Im sorry, I couldnt process that. Could we try again?\n\nWould you like to continue talking about this or share something else?', '2025-01-18 05:21:29');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(50) NOT NULL,
  `usertype` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`login_id`, `username`, `password`, `usertype`) VALUES
(1, 'admin', 'admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `user_reg`
--

CREATE TABLE `user_reg` (
  `user_reg_id` int(11) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `place` varchar(100) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_reg`
--

INSERT INTO `user_reg` (`user_reg_id`, `first_name`, `last_name`, `gender`, `place`, `phone`, `email`, `username`, `password`) VALUES
(1, 'sam', 'john', 'male', 'ekm', '9087654321', 'sam@gmail.com', 'sam', 'sam');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `chat`
--
ALTER TABLE `chat`
  ADD PRIMARY KEY (`chat_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`login_id`);

--
-- Indexes for table `user_reg`
--
ALTER TABLE `user_reg`
  ADD PRIMARY KEY (`user_reg_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `chat`
--
ALTER TABLE `chat`
  MODIFY `chat_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `login_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `user_reg`
--
ALTER TABLE `user_reg`
  MODIFY `user_reg_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
