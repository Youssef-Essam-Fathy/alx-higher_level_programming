-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
CREATE database IF NOT EXISTS hbtn_0d_usa;
CREATE table IF NOT EXISTS hbtn_0d_usa.cities
(
`id` INT PRIMARY KEY UNIQUE NOT NULL,
`name` VARCHAR(256) NOT NULL,
`state_id` INT NOT NULL,
FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id));