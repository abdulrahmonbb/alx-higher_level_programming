#!/usr/bin/python3

"""
This script takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Accesses the database, lists all the cities
    of a state passed as argument.
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
        "SELECT cities.id, cities.name FROM cities JOIN states \
            ON cities.state_id=states.id WHERE states.name \
            LIKE BINARY %(state_name)s ORDER BY cities.id", {'state_name': argv[4]}
    )

    cities = cursor.fetchall()

    print(", ".join(city[1] for city in cities))
