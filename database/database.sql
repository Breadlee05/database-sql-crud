CREATE DATABASE IF NOT EXISTS student_db;
USE student_db;

CREATE TABLE IF NOT EXISTS students (
    roll_number INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    email VARCHAR(100)
);
