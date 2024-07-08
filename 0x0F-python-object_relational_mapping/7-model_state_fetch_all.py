#!/usr/bin/python3

"""
This script lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Build database url
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    # Create the engine
    engine = create_engine(db_url)

    # Create a session class and bind to  the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Loop through the results of the query and print each object
    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")

    session.close()
