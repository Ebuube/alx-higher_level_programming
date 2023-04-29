-- Create a database and create a table

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	CONSTRAINT cities_pk PRIMARY KEY (id),
	CONSTRAINT cities_states_fk FOREIGN KEY (id)
	REFERENCE states (id)
);
