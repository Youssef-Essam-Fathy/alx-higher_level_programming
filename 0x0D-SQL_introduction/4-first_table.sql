-- creates a table called first_table in the current database in my MySQL server
CREATE first_table (id, name) VALUES (INT, VARCHAR(256)) IF NOT EXISTS first_table;