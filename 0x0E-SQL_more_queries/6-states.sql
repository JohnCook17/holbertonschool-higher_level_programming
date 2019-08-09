-- Creates a new db and table if they dont exist
-- Creates a new db and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (`id` INT NOT NULL AUTO_INCREMENT UNIQUE, `name` VARCHAR(256) NOT NULL,PRIMARY KEY (`id`))