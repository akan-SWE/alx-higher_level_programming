-- Displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- Assuming the dump file (table) is in the database

SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY city ORDER BY avg_temp DESC
LIMIT 3;

