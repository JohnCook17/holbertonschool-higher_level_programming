-- counts the number of a specific score
-- prints the number of instances of a score
SELECT `score`, count(`score`) AS `number` FROM second_table GROUP BY `score` DESC;
