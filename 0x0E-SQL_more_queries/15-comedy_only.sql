-- List all Comedy shows in the database

SELECT tv_shows.title
FROM (tv_genres
	JOIN tv_show_genres
	ON tv_show_genres.genre_id = tv_genres.id
	AND tv_genres.name = 'Comedy')
JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC;
