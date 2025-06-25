-- ists all genres of the show Dexter.
SELECT name FROM tv_genres tg 
WHERE tg.id IN (
	SELECT tsg.genre_id
	FROM tv_show_genres tsg
	WHERE tsg.show_id = 
	(SELECT id
	FROM tv_shows ts
	WHERE ts.title ='Dexter'))
ORDER BY name;
