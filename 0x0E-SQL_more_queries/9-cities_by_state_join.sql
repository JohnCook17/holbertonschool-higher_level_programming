-- A script that list all cities in the database
-- Combines the two tables to list all the info
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON states.id = cities.state_id  ORDER BY cities.id ASC;
