-- list all genres of a show
-- use where to specify show
SELECT tv_genres.name FROM tv_genres LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id RIGHT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id WHERE tv_shows.title = "Dexter" ORDER BY tv_genres.name ASC;
