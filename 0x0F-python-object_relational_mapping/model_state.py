#!/usr/bin/python3
"""
Module: model_state.py

Defines a State class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """Defines a state class that maps to the states table
    Attribute:
        id - Unique identification number for each entry
        name - The name of the state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
