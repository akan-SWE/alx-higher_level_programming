-- Lists all records with a score >= 10 in the table second_table of the 
-- database hbtn_0c_0 in your MySQL server.
-- Record displays both score and name
-- Result is ordered by score (top first)
SELECT score, name FROM `second_table`
WHERE score >= 10
ORDER BY score DESC;
