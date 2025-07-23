CREATE DATABASE IF NOT EXISTS attendance_db_python;

USE attendance_db_python;

CREATE TABLE IF NOT EXISTS attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    time TIME,
    date DATE
);

select * from attendance;

-- drop table attendance;