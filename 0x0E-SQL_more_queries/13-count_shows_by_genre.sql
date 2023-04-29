-- List all genres from the database and display the number of shows linked to each
SELECT tv_genres.name AS 'TV Show genre',
	count(tv_genres.id) AS 'Number of shows linked to this genre'
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
ORDER BY 'Number of shows linked to this genre' DESC;
