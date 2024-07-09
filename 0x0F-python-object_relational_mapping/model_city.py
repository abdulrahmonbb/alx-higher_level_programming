#!/usr/bin/python3

"""
This script contains the class definition of a City.
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    Represents the cities table in the database.

    Attributes:
    __tablename__ (str): represents the name of the table
        id (int): id of the class
        name (int): name of the class
        state_id: represents the id of the state that
            corresponds with the city in the states table.
    """

    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
