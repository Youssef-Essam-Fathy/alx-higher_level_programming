--  lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT name
FROM hbtn_0d_usa.states
WHERE name='California'
ORDER BY hbtn_0d_usa.cities.id ASC;