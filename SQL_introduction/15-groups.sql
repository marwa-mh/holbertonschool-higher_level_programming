-- lists the number of records with the same score in the table
SELECT score, COUNT(id) 'number'
FROM second_table
GROUP BY score
ORDER by number DESC;