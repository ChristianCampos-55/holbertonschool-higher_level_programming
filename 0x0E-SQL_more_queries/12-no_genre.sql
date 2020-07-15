-- Lists all shows in 'hbtn_0d_tvshows'
-- shows must not have a genre linked
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
WHERE tv_show_genres.genre_id is NULL ORDER BY tv_shows.title;
