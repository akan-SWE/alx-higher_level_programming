-- Lists all records of the table 'second_table' of the database 'hbtn_0c_0' in the MySQL server.
-- Don’t list rows without a name value
-- Display the score and the name (in this order)
-- Listed by descending score
SELECT score, name FROM `second_table`
WHERE name is NOT NULL
ORDER BY score DESC;

