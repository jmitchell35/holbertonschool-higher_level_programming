-- Task 1
-- Write a script that creates the MySQL server user user_0d_1.

-- Creates the user only if it doesn't already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- Apply the privilege changes
FLUSH PRIVILEGES;