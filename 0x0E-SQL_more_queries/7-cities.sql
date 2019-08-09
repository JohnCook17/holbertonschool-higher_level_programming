-- Creates a db if not exist and a table in the db
-- Uses a foreign key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use
USE hbtn_0d_usa;
-- creates table
CREATE TABLE IF NOT EXISTS cities
(id INT UNIQUE AUTO_INCREMENT NOT NULL, 
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL, 
FOREIGN KEY (state_id) REFERENCES states(id), 
PRIMARY KEY (id));
