-- lists all cities contained in the database hbtn_0d_usa
SELECT c.id, c.name, s.name
FROM cities AS c
INNER JOIN states AS s ON cities.state_id=state_id
ORDER BY c.id;