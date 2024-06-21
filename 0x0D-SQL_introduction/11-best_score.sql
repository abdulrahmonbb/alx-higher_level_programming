-- Lists all records of the table second_table  with score >= 10 in the database hbtn_0c_0 in our MySQL server

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC
