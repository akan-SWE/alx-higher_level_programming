-- Creates the MySQL server user user_0d_1 if the user doesn't exists
-- 
-- user_0d_1 have all privileges on your MySQL server
-- The user_0d_1 password is set to user_0d_1_pwd

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

