-- Create a database and city with foreign key
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `cities` (
	id	INT AUTO_INCREMENT NOT NULL,
	state_id	INT NOT NULL,
	name	VARCHAR(256) NOT NULL,
	CONSTRAINT id_uk UNIQUE KEY (id),
	CONSTRAINT id_pk PRIMARY KEY (id),
	CONSTRAINT cities_states_fk
		FOREIGN KEY (state_id)
		REFERENCES states (id));
