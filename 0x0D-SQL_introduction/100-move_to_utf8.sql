-- Converts hbtn_0c_0 database, first_table and name field to UTF8 
-- (utf8mb4, collate utf8mb4_unicode_ci) -- in the MySQL server.
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

