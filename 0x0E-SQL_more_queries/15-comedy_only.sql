-- Lists all Comedy shows in the database hbtn_0d_tvshows.
--
-- The tv_genres table contains only one record where name = Comedy
-- (but the id can be different)
-- Each record should display: tv_shows.title
-- Results is sorted in ascending order by the show title.

SELECT ts.title
FROM tv_shows ts
JOIN tv_show_genres tsg ON ts.id = tsg.show_id
JOIN tv_genres tg ON tsg.genre_id = tg.id
WHERE tg.name = 'Comedy'
ORDER BY ts.title
