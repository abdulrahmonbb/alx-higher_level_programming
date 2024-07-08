#!/usr/bin/python3

"""
This script lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    db_url = "mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    letter = 'a'
    for state in session.query(State).order_by(State.id):
        if letter in state.name:
            print("{}: {}".format(state.id, state.name))
