-- Table Creation for MariaDB Instance Compatible with DataJoint Manipulation
-- Written with the assistance and support of Ed O'Donnell, Kleinfeld Lab UCSD (eodonnell@health.ucsd.edu)
-- Author: Jeremy Delahanty, Tye Lab, Salk Institute of Biological Sciences (jdelahanty@salk.edu)
-- Created: 3/5/2021

-- TODO: Finish behavior_twop table
-- TODO: Finish behavior_social table
-- TODO: Finish twop table
-- TODO: Build twop_config table
-- TODO: Evaluate surgery tables

--
-- Drop Tables if Necessary
--

--DROP TABLE IF EXISTS mouse;
--DROP TABLE IF EXISTS experimenter;
--DROP TABLE IF EXISTS surgery;
--DROP TABLE IF EXISTS behavior_social;
--DROP TABLE IF EXISTS behavior_twop;
--DROP TABLE IF EXISTS twop;



---- BUILD TABLES ----


--
-- Table structure for table mouse
--

CREATE TABLE mouse (
  id int(11) NOT NULL AUTO_INCREMENT,
  sex enum('M','F') DEFAULT NULL,
  species varchar(10) DEFAULT 'Mice',
  strain varchar(50) DEFAULT NULL,
  vendor varchar(20) DEFAULT NULL,
  age int(11) DEFAULT 56,
  arrived_on date DEFAULT NULL,
  order_no varchar(20) DEFAULT NULL,
  ard_id varchar(10) DEFAULT NULL,
  cage_id int(11) DEFAULT NULL,
  exp_code enum('exp', 'con') DEFAULT NULL,
  active tinyint(4) NOT NULL DEFAULT 1,
  created datetime(6) NOT NULL,
  updated timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table mouse_weights
--

CREATE TABLE mouse_weight (
  id int(11) NOT NULL AUTO_INCREMENT,
  mouse_id int(11) NOT NULL,
  mouse_weight int(5) DEFAULT NULL,
  active tinyint(4) NOT NULL DEFAULT 1,
  created datetime(6) NOT NULL,
  updated timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (id),
  KEY K__mouse_weight_mouse_id (mouse_id),
  
  CONSTRAINT FK__mouse_weight_mouse_id FOREIGN KEY (mouse_id) REFERENCES mouse (id) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table experimenter
--

CREATE TABLE experimenter (
  id int(8) NOT NULL AUTO_INCREMENT,
  name varchar(20) DEFAULT NULL,
  sex enum('M', 'F') DEFAULT NULL,
  active tinyint(4) NOT NULL DEFAULT 1,
  created datetime(6) NOT NULL,
  updated timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table surgery
--

CREATE TABLE surgery (
  id int(11) NOT NULL AUTO_INCREMENT,
  mouse_id int(11) NOT NULL,
  experimenter_id int(8) NOT NULL,
  session_date_start datetime(6) NOT NULL,
  session_date_end datetime(6),
  surgery_type varchar(255) DEFAULT NULL,
  bregma DOUBLE(6,3) DEFAULT NULL,
  level_left DOUBLE(6,3) DEFAULT NULL,
  level_right DOUBLE(6,3) DEFAULT NULL,
  level_z DOUBLE(6,3) DEFAULT NULL,
  surgery_notes varchar(255) DEFAULT NULL,
  surgery_path varchar(255) DEFAULT NULL,
  active tinyint(4) NOT NULL DEFAULT 1,
  created datetime(6) NOT NULL,
  updated timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (id),
  KEY K__surgery_mouse_id (mouse_id),
  KEY K__surgery_experimenter_id (experimenter_id),

  CONSTRAINT FK__surgery_mouse_id FOREIGN KEY (mouse_id) REFERENCES mouse (id) ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT FK__surgery_experimenter_id FOREIGN KEY (experimenter_id) REFERENCES experimenter (id) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table Structure for injections during surgery
--

CREATE TABLE surgery_injections(
  id int(11) NOT NULL AUTO_INCREMENT,
  surgery_id int(11) NOT NULL,
  drug_type varchar(20) DEFAULT NULL,
  drug_target varchar(20) DEFAULT NULL,
  drug_method varchar(20) DEFAULT NULL,
  drug_dose DOUBLE(6,3) DEFAULT NULL,
  drug_volume DOUBLE(6,3) DEFAULT NULL,
  drug_bilateral BIT DEFAULT NULL,
  ap DOUBLE(6,3) DEFAULT NULL,
  ml DOUBLE(6,3) DEFAULT NULL,
  dv DOUBLE(6,3) DEFAULT NULL,
  injection_notes varchar(255) DEFAULT NULL,
  injection_success BIT DEFAULT NULL,
  active tinyint(4) NOT NULL DEFAULT 1,
  created datetime(6) NOT NULL,
  updated timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (id),
  KEY K__surgery_injections_surgery_id (surgery_id),
  
  CONSTRAINT FK__surgery_injections_surgery_id FOREIGN KEY (surgery_id) REFERENCES surgery (id) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
  
--
-- Table structure for surgery implants
--

CREATE TABLE surgery_implants(
  id int(11) NOT NULL AUTO_INCREMENT,
  surgery_id int(11) NOT NULL,
  implant_type varchar(20) DEFAULT NULL,
  implant_target varchar(10) DEFAULT NULL,
  implant_weight tinyint(2) DEFAULT NULL,
  ap DOUBLE(6,3) DEFAULT NULL,
  ml DOUBLE(6,3) DEFAULT NULL,
  dv DOUBLE(6,3) DEFAULT NULL,
  implant_notes varchar(255) DEFAULT NULL,
  implant_success BIT DEFAULT NULL,
  active tinyint(4) NOT NULL DEFAULT 1,
  created datetime(6) NOT NULL,
  updated timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (id),
  KEY surgery_implants_surgery_id (surgery_id),
  
  CONSTRAINT FK__surgery_implants_surgery_id FOREIGN KEY (surgery_id) REFERENCES surgery (id) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for social behavior
--

CREATE TABLE behavior_social (
  id int(11) NOT NULL AUTO_INCREMENT,
  mouse_id int(11) NOT NULL,
  experimenter_id int(8) DEFAULT NULL,
  session_date datetime(6) NOT NULL,
  vid_path varchar(255) DEFAULT NULL,
  active tinyint(4) NOT NULL DEFAULT 1,
  created datetime(6) NOT NULL,
  updated timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (id),
  KEY K__behavior_social_mouse_id (mouse_id),
  KEY K__behavior_social_experimenter_id (experimenter_id),

  CONSTRAINT FK__behavior_social_mouse_id FOREIGN KEY (mouse_id) REFERENCES mouse (id) ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT FK__behavior_social_experimenter_id FOREIGN KEY (experimenter_id) REFERENCES experimenter (id) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for 2P behavior
--

CREATE TABLE behavior_twop (
  id int(11) NOT NULL AUTO_INCREMENT,
  mouse_id int(11) NOT NULL,
  experimenter_id int(8) DEFAULT NULL,
  session_date datetime(6) NOT NULL,
  vid_path varchar(255) DEFAULT NULL,
  active tinyint(4) NOT NULL DEFAULT 1,
  created datetime(6) NOT NULL,
  updated timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (id),
  KEY K__behavior_twop_mouse_id (mouse_id),
  KEY K__behavior_twop_experimenter_id (experimenter_id),

  CONSTRAINT FK__behavior_twop_mouse_id FOREIGN KEY (mouse_id) REFERENCES mouse (id) ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT FK__behavior_twop_experimenter_id FOREIGN KEY (experimenter_id) REFERENCES experimenter (id) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for 2P imaging data
--

CREATE TABLE twop (
  id int(11) NOT NULL AUTO_INCREMENT,
  mouse_id int(11) NOT NULL,
  experimenter_id int(8) DEFAULT NULL,
  session_date datetime(6),
  vid_path varchar(255) DEFAULT NULL,
  active tinyint(4) NOT NULL DEFAULT 1,
  created datetime(6) NOT NULL,
  updated timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (id),
  KEY K__twop_mouse_id (mouse_id),
  KEY K__twop_experimenter_id (experimenter_id),

 CONSTRAINT FK__twop_mouse_id FOREIGN KEY (mouse_id) REFERENCES mouse (id) ON UPDATE CASCADE ON DELETE CASCADE,
 CONSTRAINT FK__twop_experimenter_id FOREIGN KEY (experimenter_id) REFERENCES experimenter (id) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--CREATE TABLE `twop_analysis_config` (
--  `id` int PRIMARY KEY AUTO_INCREMENT,
--  `twop_session` int NOT NULL,
--  `config_path` varchar(255),
--  `notes` varchar(255),
--  `active` tinyint(4) NOT NULL DEFAULT 1,
--  `created` datetime(8) NOT NULL,
--  `updated` timestamp DEFAULT NULL,
--  `primary` key(id)
--);
