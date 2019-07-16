-- Creates a new table with a forced unique id
-- uses unique
CREATE TABLE IF NOT EXISTS `unique_id` (`id` INT DEFAULT 1 UNIQUE, `name` VARCHAR(256));
