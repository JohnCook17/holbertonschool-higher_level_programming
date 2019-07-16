-- avg temp F of city
-- displays the average temp of a city ordered by desc
SELECT `city`, AVG(`value`) AS "avg_temp" FROM temperatures GROUP BY `city` ORDER BY AVG(`value`) DESC;
