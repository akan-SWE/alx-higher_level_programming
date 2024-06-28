#!/usr/bin/python3
"""
Module: relationship_city.py

Defines a City class
"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """"
    Defines a City class that maps to the cities table
    Attribute:
        id (int): Unique identification number for each state.
        name (str): The name of the state.
        state_id (int) - Reference to a State object for each entry
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
