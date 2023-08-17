-- Dump cities and states table values
-- it builds on existing data if any
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;

-- Create tables
CREATE TABLE IF NOT EXISTS `states` (
	id	INT AUTO_INCREMENT NOT NULL,
	name	VARCHAR(256) NOT NULL,
	CONSTRAINT id_uk UNIQUE KEY (id),
	CONSTRAINT id_pk PRIMARY KEY (id));

CREATE TABLE IF NOT EXISTS `cities` (
	id	INT AUTO_INCREMENT NOT NULL,
	state_id	INT NOT NULL,
	name	VARCHAR(256) NOT NULL,
	CONSTRAINT id_uk UNIQUE KEY (id),
	CONSTRAINT id_pk PRIMARY KEY (id),
	CONSTRAINT cities_states_fk FOREIGN KEY (state_id)
		REFERENCES states(id));

-- Insert records into the states table
INSERT INTO `states` (name) VALUES
	('California'),
	('Arizona'),
	('Texas'),
	('Utah');

-- Insert records into the cities table
INSERT INTO `cities` (state_id, name) VALUES
	(1, 'San Francisico'),
	(1, 'San Jose'),
	(2, 'Page'),
	(3, 'Paris'),
	(3, 'Houston'),
	(3, 'Dallas');
