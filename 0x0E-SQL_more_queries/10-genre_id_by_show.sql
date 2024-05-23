-- Lists all shows contained in hbtn_0d_tvshows that have at least
-- one genre linked.
--
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results is sorted in ascending order by tv_shows.title and tv_show_genres.genre_id


SELECT ts.title, tsg.genre_id FROM tv_shows ts
JOIN tv_show_genres tsg ON ts.id = tsg.show_id
JOIN tv_genres tg ON tsg.genre_id = tg.id
ORDER BY ts.title, tsg.genre_id;

