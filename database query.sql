CREATE DATABASE contact_saver;
USE contact_saver;
CREATE TABLE contacts(
id INT PRIMARY KEY 
AUTO_INCREMENT,
name VARCHAR(120) NOT NULL,
phone VARCHAR(17) NOT NULL,
email VARCHAR(150)
);
SELECT *from contacts;
SELECT COUNT(*)FROM contacts;