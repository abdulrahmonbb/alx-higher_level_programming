#!/usr/bin/python3

"""
This script  lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Accesses the database, Lists rows from a table,
    Where name starts with 'N'
    """

    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE states.name LIKE BINARY 'N%' \
                ORDER BY id;"

    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)
