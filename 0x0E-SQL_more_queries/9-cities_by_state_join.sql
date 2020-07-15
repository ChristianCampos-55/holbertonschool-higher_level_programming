-- list all cities in 'hbtn_0d_usa' database
SELECT cities.id, cities.name, states.name
FROM states RIGHT JOIN cities ON states.id = cities.state_id;
