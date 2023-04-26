-- List only the records from the `score` and the `name` fields of the second_table
-- Ordered by `score` in descending order
-- Only list records with score >= 10
SELECT `score`, `name` FROM `second_table`
	WHERE `score` >= 10
	ORDER BY `score` DESC;
