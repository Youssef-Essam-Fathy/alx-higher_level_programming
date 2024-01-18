-- creates the MySQL server user user_0d_1
IF 'user_0d_1' NOT EXISTS
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd'
GRANT ALL PRIVILEGES ON hbtn_0c_0.* TO 'user_0d_1'@'localhost';