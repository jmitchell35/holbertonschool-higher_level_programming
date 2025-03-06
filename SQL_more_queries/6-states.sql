-- Task 6
-- Write a script that creates the database hbtn_0d_usa and the table states
-- (in the database hbtn_0d_usa) on your MySQL server.
-- Details inside README file

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Switch to the database
USE hbtn_0d_usa;
-- Create states table if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);