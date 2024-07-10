#!/usr/bin/python3

"""
This script prints all City objects
from database `hbtn_0e_14_usa`.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    """
    Accesses the database, creates a state and city
    """

    db_url = "mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]
    )

    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cal_state = State(name='California')
    sfr_city = City(name='San Fracisco')
    cal_state.cities.append(sfr_city)

    session.add(cal_state)
    session.commit()
    session.close()
