#!/usr/bin/python3

"""
This script that lists all cities from the database hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Accesses the database, lists all entries
    from the cities table.
    """

    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM cities \
            JOIN states ON cities.state_id=states.id \
            ORDER BY cities.id"
    )

    cities = cursor.fetchall()

    for city in cities:
        print(city)
