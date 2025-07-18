-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 14, 2022 at 01:55 PM
-- Server version: 5.7.36
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fake_job_detection_webscrapping`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=41 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add user', 7, 'add_user'),
(26, 'Can change user', 7, 'change_user'),
(27, 'Can delete user', 7, 'delete_user'),
(28, 'Can view user', 7, 'view_user'),
(29, 'Can add url', 8, 'add_url'),
(30, 'Can change url', 8, 'change_url'),
(31, 'Can delete url', 8, 'delete_url'),
(32, 'Can view url', 8, 'view_url'),
(33, 'Can add feedback', 9, 'add_feedback'),
(34, 'Can change feedback', 9, 'change_feedback'),
(35, 'Can delete feedback', 9, 'delete_feedback'),
(36, 'Can view feedback', 9, 'view_feedback'),
(37, 'Can add survey', 10, 'add_survey'),
(38, 'Can change survey', 10, 'change_survey'),
(39, 'Can delete survey', 10, 'delete_survey'),
(40, 'Can view survey', 10, 'view_survey');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'jobseakerapp', 'user'),
(8, 'jobseakerapp', 'url'),
(9, 'jobseakerapp', 'feedback'),
(10, 'jobseakerapp', 'survey');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-12-10 05:53:11.748567'),
(2, 'auth', '0001_initial', '2022-12-10 05:53:12.544799'),
(3, 'admin', '0001_initial', '2022-12-10 05:53:12.765151'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-12-10 05:53:12.775165'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-12-10 05:53:12.782647'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-12-10 05:53:12.866749'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-12-10 05:53:12.928878'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-12-10 05:53:12.973481'),
(9, 'auth', '0004_alter_user_username_opts', '2022-12-10 05:53:12.978478'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-12-10 05:53:13.023247'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-12-10 05:53:13.024246'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-12-10 05:53:13.029297'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-12-10 05:53:13.083295'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-12-10 05:53:13.126104'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-12-10 05:53:13.165000'),
(16, 'auth', '0011_update_proxy_permissions', '2022-12-10 05:53:13.171997'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-12-10 05:53:13.227187'),
(18, 'jobseakerapp', '0001_initial', '2022-12-10 05:53:13.472132'),
(19, 'jobseakerapp', '0002_alter_url_user_url', '2022-12-10 05:53:13.481779'),
(20, 'sessions', '0001_initial', '2022-12-10 05:53:13.557326'),
(21, 'jobseakerapp', '0003_url_company_logo', '2022-12-10 06:08:26.266573'),
(22, 'jobseakerapp', '0004_remove_url_company_logo', '2022-12-10 06:10:49.580820'),
(23, 'jobseakerapp', '0005_rename_user_status_user_user_otp_status', '2022-12-12 06:45:52.627078'),
(24, 'jobseakerapp', '0006_rename_user_otp_status_user_user_otp', '2022-12-12 10:12:10.709507'),
(25, 'jobseakerapp', '0007_user_user_otp_status_alter_user_user_otp', '2022-12-12 10:25:53.927147'),
(26, 'jobseakerapp', '0008_remove_user_user_otp', '2022-12-12 10:26:58.508888'),
(27, 'jobseakerapp', '0009_user_user_otp', '2022-12-12 10:30:43.776858'),
(28, 'jobseakerapp', '0010_alter_user_user_otp_status', '2022-12-12 10:31:31.225947'),
(29, 'jobseakerapp', '0011_survey', '2022-12-13 05:35:00.735664'),
(30, 'jobseakerapp', '0012_alter_survey_option1_alter_survey_option10_and_more', '2022-12-13 11:24:41.216408');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('zls2stmw4som4nhrm7ocgy702istm38c', 'eyJ1c2VyX2lkIjoxfQ:1p3spA:34V4lB0xwoceh8lanWGg8m8RfNPGxvP1sXk0Q4o7-7k', '2022-12-24 05:55:00.299734'),
('h552stuh55sbixkzbnd4zz690svpw25a', 'eyJ1c2VyX2lkIjoxMH0:1p5S9G:uC29RTyvigm1Gthfw0G_qzLCoDePnbLJiLl3FVG0n8M', '2022-12-28 13:50:14.020065'),
('4uildpa26957hcfnuseaa1gly4xwy8w2', 'eyJ1c2VyX2lkIjoyMn0:1p56PI:nh1zHQqXnFg0RvBT6HU0OkrqSymf4-w2MdFZvmvo65E', '2022-12-27 14:37:20.133652');

-- --------------------------------------------------------

--
-- Table structure for table `feedback_details`
--

DROP TABLE IF EXISTS `feedback_details`;
CREATE TABLE IF NOT EXISTS `feedback_details` (
  `feed_id` int(11) NOT NULL AUTO_INCREMENT,
  `feed_desc` longtext NOT NULL,
  `feed_rating` varchar(100) NOT NULL,
  `feedback_sentiment` varchar(50) NOT NULL,
  `feedback_date` datetime(6) NOT NULL,
  `feedback_user_id` int(11) NOT NULL,
  PRIMARY KEY (`feed_id`),
  KEY `feedback_details_feedback_user_id_645303c9` (`feedback_user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feedback_details`
--

INSERT INTO `feedback_details` (`feed_id`, `feed_desc`, `feed_rating`, `feedback_sentiment`, `feedback_date`, `feedback_user_id`) VALUES
(1, 'Excellent\r\n', '3', 'Very Positive', '2022-12-13 09:37:23.219983', 10),
(2, 'very negative\r\n', '0', 'Negative', '2022-12-13 09:42:51.177110', 10),
(3, 'negative', '1', 'Negative', '2022-12-13 09:42:59.542394', 10),
(4, 'neutral', '2', 'Neutral', '2022-12-13 09:48:08.189704', 11),
(5, 'positive', '3', 'Positive', '2022-12-13 09:48:15.208207', 11),
(6, 'very positive', '4', 'Positive', '2022-12-13 09:48:24.868197', 11),
(7, 'worst', '0', 'Very Negative', '2022-12-13 09:49:09.742879', 11),
(8, 'excellent job', '4', 'Very Positive', '2022-12-13 09:49:21.570161', 11),
(9, 'Great Job', '3', 'Very Positive', '2022-12-13 14:22:29.672978', 22),
(10, 'very good', '3', 'Very Positive', '2022-12-14 11:42:29.058147', 23);

-- --------------------------------------------------------

--
-- Table structure for table `survey_details`
--

DROP TABLE IF EXISTS `survey_details`;
CREATE TABLE IF NOT EXISTS `survey_details` (
  `survey_id` int(11) NOT NULL AUTO_INCREMENT,
  `option1` varchar(50) DEFAULT NULL,
  `option2` varchar(50) DEFAULT NULL,
  `option3` varchar(50) DEFAULT NULL,
  `option4` varchar(50) DEFAULT NULL,
  `option5` varchar(50) DEFAULT NULL,
  `option6` varchar(50) DEFAULT NULL,
  `option7` varchar(50) DEFAULT NULL,
  `option8` varchar(50) DEFAULT NULL,
  `option9` varchar(50) DEFAULT NULL,
  `option10` varchar(50) DEFAULT NULL,
  `option11` varchar(50) DEFAULT NULL,
  `option12` varchar(50) DEFAULT NULL,
  `user_id_id` int(11) NOT NULL,
  PRIMARY KEY (`survey_id`),
  KEY `survey_details_user_id_id_8949ed7a` (`user_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `survey_details`
--

INSERT INTO `survey_details` (`survey_id`, `option1`, `option2`, `option3`, `option4`, `option5`, `option6`, `option7`, `option8`, `option9`, `option10`, `option11`, `option12`, `user_id_id`) VALUES
(1, 'Information Technology and Services', 'Part Time', 'Yes', 'Internship', 'Master\'s Degree', 'Project Intern', 'Online Website', '1000k to 5000k', 'Yes', 'Credit Card Details', 'Yes', 'Facebook', 10),
(2, 'Information Technology and Services', 'Full Time', 'Yes', 'Mid Senior Level', 'Bachelor\'s Degree', 'Product Manager', 'Online Website', 'Less Than 1000k', 'No', 'Credit Card Details', 'Nill', 'Linkedin', 10),
(14, 'Information Technology and Services', 'Intern', 'Yes', 'Internship', 'Master\'s Degree', 'Product Manager', 'Online Website', '10,000k Above', 'Yes', 'Photo and Media', 'No', 'Indeed', 23),
(13, 'Computer Software', 'Part Time', 'No', 'Not Applicable', 'High School', 'Sales Executive', 'Social Media', '10,000k Above', 'No', 'Photo and Media', 'Nill', 'Instagram', 22),
(12, 'Information Technology and Services', 'Part Time', 'Yes', 'Internship', 'High School', 'Research associate', 'Online Website', '10,000k Above', 'No', 'Credit Card Details', 'Nill', 'Indeed', 19);

-- --------------------------------------------------------

--
-- Table structure for table `url_deatils`
--

DROP TABLE IF EXISTS `url_deatils`;
CREATE TABLE IF NOT EXISTS `url_deatils` (
  `url_id` int(11) NOT NULL AUTO_INCREMENT,
  `url` longtext NOT NULL,
  `user_url_id` int(11) NOT NULL,
  PRIMARY KEY (`url_id`),
  KEY `URL_Deatils_user_url_id_4397bdd4` (`user_url_id`)
) ENGINE=MyISAM AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `url_deatils`
--

INSERT INTO `url_deatils` (`url_id`, `url`, `user_url_id`) VALUES
(1, 'https://internshala.com/job/detail/remote-digital-marketing-specialist-fresher-jobs-at-aantriksh1670063789', 1),
(2, 'https://internshala.com/job/detail/remote-digital-marketing-specialist-fresher-jobs-at-aantriksh1670063789', 1),
(3, 'https://internshala.com/job/detail/inside-sales-specialist-fresher-jobs-in-multiple-locations-at-skill-lync1667460462', 1),
(4, 'https://internshala.com/job/detail/inside-sales-specialist-fresher-jobs-in-multiple-locations-at-skill-lync1667460462', 1),
(5, 'https://internshala.com/job/detail/field-sales-executive-fresher-jobs-in-bangalore-at-qa-solvers1670578890', 1),
(6, 'https://internshala.com/job/detail/business-development-executive-fresher-jobs-in-bangalore-at-pure-tru-herb-private-limited1670491488', 1),
(7, 'https://internshala.com/job/detail/business-development-executive-fresher-jobs-in-bangalore-at-pure-tru-herb-private-limited1670491488', 1),
(8, 'https://internshala.com/job/detail/business-development-executive-fresher-jobs-in-bangalore-at-pure-tru-herb-private-limited1670491488', 1),
(9, 'https://internshala.com/job/detail/business-development-executive-fresher-jobs-in-bangalore-at-pure-tru-herb-private-limited1670491488', 1),
(10, 'https://internshala.com/job/detail/remote-alt-text-writer-fresher-jobs-at-qa-solvers1670649785', 1),
(11, 'https://internshala.com/job/detail/business-development-executive-fresher-jobs-in-bangalore-at-pure-tru-herb-private-limited1670491488', 1),
(12, 'https://internshala.com/job/detail/field-sales-executive-fresher-jobs-in-bangalore-at-qa-solvers1670578890', 1),
(13, 'https://internshala.com/job/detail/inside-sales-specialist-fresher-jobs-in-multiple-locations-at-skill-lync1667460462', 1),
(14, 'https://internshala.com/job/detail/business-development-executive-fresher-jobs-in-bangalore-at-pure-tru-herb-private-limited1670491488', 1),
(15, 'https://internshala.com/job/detail/remote-alt-text-writer-fresher-jobs-at-qa-solvers1670649785', 1),
(16, 'https://internshala.com/job/detail/business-development-executive-fresher-jobs-in-multiple-locations-at-engati1667541525', 1),
(17, 'https://internshala.com/job/detail/assistant-growth-manager-sales-fresher-jobs-in-multiple-locations-at-supr-surge1669809325', 11),
(18, 'https://internshala.com/job/detail/remote-sales-manager-fresher-jobs-at-bhanzu1670497864', 11),
(19, 'https://internshala.com/job/detail/remote-digital-marketing-specialist-fresher-jobs-at-aantriksh1670063789', 19),
(20, 'https://internshala.com/job/detail/business-development-executive-fresher-jobs-in-multiple-locations-at-engati1667541525', 20),
(21, 'https://internshala.com/job/detail/remote-sales-manager-fresher-jobs-at-bhanzu1670497864', 21),
(22, 'https://internshala.com/job/detail/remote-technical-sales-associate-fresher-jobs-at-sgmoid1670913304', 21),
(23, 'https://internshala.com/job/detail/remote-digital-marketing-executive-paid-ads-specialist-fresher-jobs-at-bosscoder-academy1670920407', 21),
(24, 'https://internshala.com/job/detail/remote-digital-marketing-executive-paid-ads-specialist-fresher-jobs-at-bosscoder-academy1670920407', 21),
(25, 'https://internshala.com/job/detail/remote-digital-marketing-executive-paid-ads-specialist-fresher-jobs-at-bosscoder-academy1670920407', 21),
(26, 'https://internshala.com/job/detail/remote-digital-marketing-executive-paid-ads-specialist-fresher-jobs-at-bosscoder-academy1670920407', 11),
(27, 'https://internshala.com/job/detail/remote-sales-manager-fresher-jobs-at-bhanzu1670497864', 11),
(28, 'https://internshala.com/job/detail/remote-digital-marketing-executive-paid-ads-specialist-fresher-jobs-at-bosscoder-academy1670920407', 11),
(29, 'https://internshala.com/job/detail/sr-software-engineer-3-years-of-experience-fresher-jobs-in-delhi-at-mim-essay1670845998', 11),
(30, 'https://internshala.com/job/detail/inside-sales-associate-fresher-jobs-in-gurgaon-at-internshala1670931877', 22),
(31, 'https://internshala.com/job/detail/remote-digital-marketing-executive-paid-ads-specialist-fresher-jobs-at-bosscoder-academy1670920407', 22),
(32, 'https://internshala.com/job/detail/inside-sales-associate-fresher-jobs-in-gurgaon-at-a', 22),
(33, 'https://internshala.com/job/detail/inside-sales-associate-fresher-jobs-in-gurgaon-at-internshala1670931877', 22),
(34, 'https://internshala.com/job/detail/remote-digital-marketing-specialist-fresher-jobs-at-aantriksh1670063789', 10),
(35, 'https://internshala.com/job/detail/remote-digital-marketing-specialist-fresher-jobs-at-aantriksh1670063789', 10),
(36, 'https://internshala.com/job/detail/remote-digital-marketing-specialist-fresher-jobs-at-aantriksh1670063789', 10),
(37, 'https://internshala.com/job/detail/associate-content-developer-english-fresher-jobs-in-multiple-locations-at-gigde-global-solutions-private-limited1671006300', 10),
(38, 'https://internshala.com/job/detail/associate-content-developer-english-fresher-jobs-in-multiple-locations-at-gigde-global-solutions-private-limited1671006300', 23),
(39, 'https://internshala.com/job/detail/communication-executive-fresher-jobs-in-delhi-at-chamber-of-commerce-sustainable-development-and-foreign-relations1670956727', 23),
(40, 'https://internshala.com/job/detail/remote-digital-marketing-specialist-fresher-jobs-at-a', 23),
(41, 'https://internshala.com/job/detail/communication-executive-fresher-jobs-in-delhi-at-chamber-of-commerce-sustainable-development-and-foreign-relations1670956727', 23),
(42, 'https://internshala.com/job/detail/communication-executive-fresher-jobs-in-delhi-at-chamber-of-commerce-sustainable-development-and-foreign-relations1670956727', 23),
(43, '        messages.success(req, \'Survey Submitted Successfully\')', 23),
(44, '        messages.success(req, \'Survey Submitted Successfully\')', 23),
(45, '     context = {\'status\':status,         \'job_details\':job_details,     \'logosrc\':logosrc,     \'job_title\':title,     \'company\':company,     \'companylinktext\':details_companylinktext,     \'company_website_link\':details_companylink,     # \'company_logo\':logo,     \'company_location\':location,     \'internship_deatils\':internshipdetails,     \'company_posted_tags\':tags,     \'about_company_title\':details_about_company_title,     \'about_company\':details_about_company,     \'company_hiring_activity\':details_company_activity,     \'skills_required\':skills_required,     \'salary\':salary,     \'openings\':openings}', 23),
(46, 'https://internshala.com/jobs/jobs-in-delhi/', 23),
(47, 'https://internshala.com/jobs/jobs-in-delhi/', 23),
(48, 'jobseaker_job_details_page', 23),
(49, 'jobseaker_job_details_page', 23),
(50, '        return redirect(\'jobseaker_job_details_page\')', 23),
(51, 'jobseaker_analyze_job_post', 23),
(52, 'https://internshala.com/jobs/jobs-in-delhi/', 23),
(53, 'https://internshala.com/job/detail/communication-executive-fresher-jobs-in-delhi-at-chamber-of-commerce-sustainable-development-and-foreign-relations1670956727', 23),
(54, 'https://internshala.com/job/detail/operations-executive-fresher-jobs-in-delhi-at-ostello-india-private-limited1670951403', 23),
(55, 'https://internshala.com/job/detail/associate-content-developer-english-fresher-jobs-in-multiple-locations-at-gigde-global-solutions-private-limited1671006300', 23),
(56, 'https://internshala.com/job/detail/communication-executive-fresher-jobs-in-delhi-at-chamber-of-commerce-sustainable-development-and-foreign-relations1670956727', 23),
(57, 'https://internshala.com/job/detail/associate-content-developer-english-fresher-jobs-in-multiple-locations-at-gigde-global-solutions-private-limited1671006300', 23),
(58, 'https://internshala.com/job/detail/operations-executive-fresher-jobs-in-delhi-at-ostello-india-private-limited1670951403', 23),
(59, 'https://internshala.com/job/detail/operations-executive-fresher-jobs-in-delhi-at-ostello-india-private-limited1670951403', 22),
(60, 'https://internshala.com/job/detail/remote-digital-marketing-specialist-fresher-jobs-at-aantriksh1670063789', 10);

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

DROP TABLE IF EXISTS `user_details`;
CREATE TABLE IF NOT EXISTS `user_details` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_username` varchar(100) NOT NULL,
  `user_email` varchar(100) NOT NULL,
  `user_password` varchar(100) NOT NULL,
  `user_contact` varchar(15) NOT NULL,
  `user_addresss` varchar(100) NOT NULL,
  `user_image` varchar(100) NOT NULL,
  `user_otp_status` varchar(50) NOT NULL,
  `user_otp` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`user_id`, `user_username`, `user_email`, `user_password`, `user_contact`, `user_addresss`, `user_image`, `user_otp_status`, `user_otp`) VALUES
(11, 'Harsha', 'harshavardhan.hv12@gmail.com', '0000', '9618294480', 'Hyderabad', 'images/user/267198504_1694302214294970_7042933464512258898_n_1_4rPrKL0.jpg', 'Accepted', '3188'),
(10, 'netra', 'netra@email.com', '0000', '9618294480', 'Hyderabad', 'images/user/10.jpg', 'Accepted', '6736'),
(22, 'vijay', 'vijay@email.com', 'Harsha03', '9618294480', 'Hyderabad', 'images/user/Kakashi_Hatake.jpg', 'Accepted', '5518'),
(23, 'kiran', 'kiran@email.com', 'Kiran12', '8744566587', 'hyderabad', 'images/user/genuine.png', 'otp verified', '8768'),
(21, 'vikram', 'vikram@email.com', 'Harsha03', '9618294480', 'Hyderabad', 'images/user/267111175_658332002189900_7198454065126109970_n_1_XYGz7FE.jpg', 'otp verified', '8480'),
(19, 'neha', 'neha@email.com', '0000', '9955998844', 'Hyderabad', 'images/user/9.jpg', 'otp is pending', '7869'),
(20, 'vishnu', 'vishnu@email.com', 'Harsha03', '9618294480', 'Hyderabad', 'images/user/IMG_20211127_001724.jpg', 'otp verified', '2303'),
(18, 'ked', 'kedar@email.com', '0000', '9618294480', 'Hyderabad', 'images/user/267943552_291287712933811_2629578141344788144_n_1_kBNjDCy.jpg', 'otp verified', '9540');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
