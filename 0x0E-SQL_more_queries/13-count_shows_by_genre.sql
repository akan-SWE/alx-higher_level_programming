-- Lists all genres from hbtn_0d_tvshows and displays the number of shows
-- linked to each.
--
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column is called genre
-- Second column is called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results is sorted in descending order by the number of shows linked.

SELECT tg.name AS genre, COUNT(*) AS number_of_shows
FROM tv_show_genres tsg
JOIN tv_genres tg ON tsg.genre_id = tg.id
GROUP BY tg.name ORDER BY number_of_shows DESC;
