-- List all cities in California
-- Uses
SELECT `id`, `name` FROM cities WHERE state_id = (SELECT id FROM states WHERE `name` = "California");