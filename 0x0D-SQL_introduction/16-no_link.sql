-- A script that lists all records of the table `second_table` of the database
-- It skips rows without a `name` value
-- The result is in descending order

SELECT score, name FROM second_table
	WHERE name IS NOT NULL
	ORDER BY `score` DESC;
