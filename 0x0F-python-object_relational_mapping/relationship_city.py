#!/usr/bin/python3

"""
This script defines a City class
to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State

class City(Base):
    """
    Represents the cities table in the database

    Attributes:
        __tablename__ (str): the name of the table
        id (int): the id of the class
        name (str): the name of the class
        state_id (int): The state the city belong to
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
