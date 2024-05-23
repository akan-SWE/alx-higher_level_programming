-- Displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- Assuming the dump file (table) is in the database

SELECT state, MAX(value) AS max_temp FROM temperatures
GROUP BY state ORDER BY state;

