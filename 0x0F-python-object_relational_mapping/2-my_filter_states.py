#!/usr/bin/python3

"""
This script  takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


if __name__ == '__main__':
    """
    Accesses the database, displays values in the table,
    that matches the last argument.
    """

    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = db.cursor()

    last_arg = sys.argv[4]

    query = "SELECT * FROM states WHERE states.name LIKE BINARY '{}' \
                ORDER BY id;".format(last_arg)
    cursor.execute(query)

    state = cursor.fetchall()
    print(state)
