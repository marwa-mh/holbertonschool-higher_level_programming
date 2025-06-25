-- lists all Comedy shows 
SELECT title
FROM tv_shows ts
JOIN tv_show_genres tsg 
ON ts.id =tsg.show_id
JOIN tv_genres tg 
ON tg.id =tsg.genre_id
WHERE tg.name LIKE 'Comedy'
ORDER BY title;
