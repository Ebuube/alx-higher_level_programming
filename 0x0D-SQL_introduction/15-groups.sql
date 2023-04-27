-- List the number of records with the same score in the table `second_table`
-- Sorted by the `number` of records in descending order
SELECT score, COUNT(score) AS `number`
	FROM second_table
	GROUP BY score
	ORDER BY `number` DESC;
