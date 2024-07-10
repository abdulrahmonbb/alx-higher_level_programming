#!/usr/bin/python3

"""
This script defines a State class and
a Base class to work with MySQLAlchemy ORM.
"""


from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents the states table in the database.

    Attributes:
        __tablename__ : the name of the table
        id (int): the id of the class
        name (str): the name of the class
        cities (:obj:`City`): The cities belong to state.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
