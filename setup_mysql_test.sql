
-- Script that creates database hbnb_test_db and user hbnb_test in localhost
-- with password hbnb_test_pwd and granting all privileges on this database
-- and select privileges on performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER
	IF NOT EXISTS 'hbnb_test'@'localhost';
ALTER USER 'hbnb_test'@'localhost'
	IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
