-- This script uses the hbtn_0d_tvshows database to--  list all genres not 
-- linked to the show Dexter.

-- The tv_shows table contains only one record where title -- = Dexter 
-- (but the id can be different)
-- Each record displays: tv_genres.name
-- Results is sorted in ascending order by the genre name

-- Read all the genres that are not among Dexter linked genres
SELECT DISTINCT tg.name 
FROM tv_shows ts
JOIN tv_show_genres tsg ON ts.id = tsg.show_id
JOIN tv_genres tg ON tsg.genre_id = tg.id
WHERE tg.name NOT IN (
	-- Read all the genres that Dexter is linked to
	SELECT tg.name 
	FROM tv_shows ts
	JOIN tv_show_genres tsg ON ts.id = tsg.show_id
	JOIN tv_genres tg ON tsg.genre_id = tg.id
	WHERE ts.title = 'Dexter'
);
ORDER BY tg.name;

