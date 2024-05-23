-- Lists all the cities of California that can be found in the database hbtn_0d_usa.
-- Results is sorted in ascending order by cities.id

SELECT c.id, c.name
FROM cities c, states s
WHERE c.state_id = 1 AND s.name = 'California'
ORDER BY c.id

