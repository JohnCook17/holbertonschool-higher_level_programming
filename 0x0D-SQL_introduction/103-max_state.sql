-- max temp of state by name
-- displays the max temp of a state by name
SELECT `state`, MAX(`value`) AS "max_temp" FROM temperatures GROUP BY `state`;