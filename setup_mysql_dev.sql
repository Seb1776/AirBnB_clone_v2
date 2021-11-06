
-- Script that creates database hbnb_dev_db and user hbnb_dev in localhost
-- with password hbnb_dev_pwd and granting all privileges on this database
-- and select privileges on performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER
	IF NOT EXISTS 'hbnb_dev'@'localhost';
ALTER USER 'hbnb_dev'@'localhost'
	IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
