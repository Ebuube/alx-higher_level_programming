-- List all genres of the show 'Dexter' from the database parsed as argument
SELECT name
FROM (tv_shows
	JOIN tv_show_genres
	ON tv_shows.title = 'Dexter'
	AND tv_show_genres.show_id = tv_shows.id)
JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_genres.name ASC;
