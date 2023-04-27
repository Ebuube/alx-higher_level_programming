-- Display the average temperature (Fahrenheit) by city ordered by temperature
-- In descending order

SELECT `city`, AVG(`value`) AS `avg_temp`
	FROM `temperatures`
	GROUP BY `city`
	ORDER BY `avg_temp` DESC;
