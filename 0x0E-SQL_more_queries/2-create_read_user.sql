-- Create the database 'hbtn_0d_2' and the user 'user_0d_2'
-- Grant only 'SELECT' privilege in the database 'hbtn_0d_2' to the user

CREATE DATABASE IF NOT EXISTS 'hbtn_0d_2';
CREATE USER IF NOT EXISTS 'user_0d_2' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON 'hbtn_0d_2'.* TO 'user_0d_2';
