-- List all genres not linked to the show 'Dexter'

WITH tb_temp AS (
	SELECT tv_genres.name
	FROM (tv_genres
		JOIN tv_show_genres
		ON tv_genres.id = tv_show_genres.genre_id)
	JOIN tv_shows
	ON tv_shows.id = tv_show_genres.show_id
	AND tv_shows.title NOT IN ('Dexter'))
SELECT DISTINCT tb_temp.name
FROM tb_temp
ORDER BY tb_temp.name ASC;
