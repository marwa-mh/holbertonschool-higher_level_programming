-- script that lists all the cities of California
SELECT id, name
FROM cities
WHERE state_id = (SELECT id
                FROM states
                WHERE name LIKE 'California')
ORDER BY id;
