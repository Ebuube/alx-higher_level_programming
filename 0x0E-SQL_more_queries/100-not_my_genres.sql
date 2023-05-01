-- List all genres not linked to the show 'Dexter'

WITH tb_temp AS (
	SELECT *
	FROM tv_genres
	JOIN tv_show_genres
	ON tv_show_genres.genre_id = tv_genres.id)
SELECT tb_temp.name
FROM tb_temp
JOIN tv_shows
ON tv_shows.title != 'Dexter'
AND tv_shows.id = tb_temp.show_id
GROUP BY tb_temp.name
ORDER BY tb_temp.name;
