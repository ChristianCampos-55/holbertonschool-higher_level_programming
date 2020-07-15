-- Lists all comedy shows in 'hbtn_0d_tvshows' database
SELECT shows.title FROM tv_genres AS genres JOIN tv_show_genres
ON genres.id = tv_show_genres.genre_id JOIN tv_shows AS shows
ON tv_show_genres.show_id = shows.id WHERE genres.name = "Comedy" ORDER BY 1;
