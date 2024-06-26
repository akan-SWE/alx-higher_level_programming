-- Creates the database hbtn_0d_2 and the user user_0d_2 if there exists
-- respectively.
-- user_0d_2 has only SELECT privilege in the database hbtn_0d_2
-- The user_0d_2 password is set to user_0d_2_pwd

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

