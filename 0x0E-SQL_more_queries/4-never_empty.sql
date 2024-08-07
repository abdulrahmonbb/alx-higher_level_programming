-- This script creates a tale 'id-not-null'
-- id_not_null description:
  -- id INT
  -- name VARCHAR
-- The database name will be passed as an argument of the mysql command
-- If the table id_not_null already exists, your script should not fail

CREATE TABLE IF NOT EXISTS id_not_null (
  id INT DEFAULT 1,
  name VARCHAR(256)
);
