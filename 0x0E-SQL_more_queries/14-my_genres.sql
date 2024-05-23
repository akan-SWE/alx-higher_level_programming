-- Script that uses the hbtn_0d_tvshows database to
-- lists all genres of the show Dexter.
--
-- The tv_shows table contains only one record where title = Dexter
-- (but the id can be different)
-- Results must be sorted in ascending order by the genre name.

SELECT tg.name
FROM tv_shows ts
JOIN tv_show_genres tsg ON ts.id = tsg.show_id
JOIN tv_genres tg ON tsg.genre_id = tg.id
WHERE ts.title LIKE 'Dexter'
ORDER BY tg.name
