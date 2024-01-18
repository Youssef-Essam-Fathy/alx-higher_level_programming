-- creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
CREATE database IF NOT EXISTS hbtn_0d_usa;
CREATE table IF NOT EXISTS hbtn_0d_usa.states(`id` INT PRIMARY KEY UNIQUE AUTO_INCREMENT NOT NULL, `name` VARCHAR(256) NOT NULL);