#!/usr/bin/python3

"""
This script lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == '__main__':
    """
    Accesses the database and lists the rows from the states table.
    """

    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute a query
    query = "SELECT * FROM states ORDER BY id;"
    cursor.execute(query)

    # Fetch the results
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)
