-- Task 5
-- Write a script that creates the table unique_id on your MySQL server.
-- Details inside README file
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);