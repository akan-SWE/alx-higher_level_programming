-- Creates a table 'second_table' in the database 'hbtn_0c_0' in the MySQL
-- server and add multiple rows.

-- creates table 'second_table`
CREATE TABLE IF NOT EXISTS `second_table`
(
	id INT,
	name VARCHAR(256),
	score INT
);
-- inserts multiple rows in 'second_table'
INSERT INTO `second_table`
VALUES	(1, 'John', 10),
	(2, 'Alex', 3),
	(3, 'Bob', 14),
	(4, 'George', 8);

