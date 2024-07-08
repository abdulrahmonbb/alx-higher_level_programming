#!/usr/bin/python3

"""
This script contains the class definition of a
State and an instance Base = declarative_base()
"""


from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class State(Base):
    """
    Represents the states table in the database.

    Attributes:
        __tablename__ (str): The table name of the class.
        id (int): The State id of the class.
        name (str): The state name of the class.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
