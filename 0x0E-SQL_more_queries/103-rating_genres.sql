-- Lists all genres in the database hbtn_0d_tvshows_rate
-- by their rating.
--
-- Each record displays: tv_genres.name - rating sum
-- Results is sorted in descending order by their rating

SELECT tg.name, SUM(rate) AS rating
FROM tv_genres tg
JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
JOIN tv_shows ts ON tsg.show_id = ts.id
JOIN tv_show_ratings tsr ON ts.id = tsr.show_id
GROUP BY tg.name
ORDER BY rating DESC;
