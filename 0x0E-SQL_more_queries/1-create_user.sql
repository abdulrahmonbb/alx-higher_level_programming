-- This script creates the user 'user_0d_1'
-- user should have all privileges on the MySQL server
-- if user already exists, script should not fail.

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
