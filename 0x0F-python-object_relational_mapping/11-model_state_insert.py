#!/usr/bin/python3

"""
This script adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


if __name__ == '__main__':
    """
    Accesses the database, adds a new object
    to the states table.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]
    )

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    print(f"{new_state.id}")
    session.close()
