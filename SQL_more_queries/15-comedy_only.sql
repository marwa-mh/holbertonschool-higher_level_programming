-- lists all Comedy shows 
SELECT title
FROM tv_shows ts 
WHERE ts.id IN (
	SELECT tsg.show_id
	FROM tv_show_genres tsg 
	WHERE tsg.genre_id =(
	SELECT tg.id
	FROM tv_genres tg
	WHERE tg.name LIKE 'Comedy'))
ORDER BY title;
