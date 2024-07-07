#!/usr/bin/python3

"""
This script takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""

import MySQLdb
import sys


if __name__ == '__main__':
    """
    Access the database, displays values in the table,
    that matches the last argument.
    Safe from SQL injections.
    """

    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE \
            BINARY %(name)s ORDER BY id", {'name': sys.argv[4]}
    )

    states = cursor.fetchall()

    for state in states:
        print(state)
