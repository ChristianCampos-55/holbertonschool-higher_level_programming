-- Lists all genres from 'hbtn_0d_tvshows' database
-- also displays the numbe of shows linked to each
SELECT tv_genres.name, COUNT(show_id) AS number_of_shows FROM tv_show_genres
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY 1 ORDER BY 2 DESC;
