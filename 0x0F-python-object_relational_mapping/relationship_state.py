#!/usr/bin/python3
"""
Module: relationship_state

Defines a State class
"""
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
# from relationship_city import City

Base = declarative_base()


class State(Base):
    """
    Defines a state class that maps to the states table
    Attributes:
        id (int): Unique identification number for each state.
        name (str): The name of the state.
        cities (list): A list of City objects that are associated with
        the state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='delete')
