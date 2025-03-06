-- Task 2
-- Write a script that creates the database hbtn_0d_2 and the user user_0d_2.
-- See details on the README.md

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant only SELECT privilege to user_0d_2 on hbtn_0d_2 database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
-- Apply the privilege changes
FLUSH PRIVILEGES;