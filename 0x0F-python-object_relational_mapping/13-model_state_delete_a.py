#!/usr/bin/python3
"""
Module: 13-model_state_delete_a

Deletes all State objects with a name containing the letter a from the
database hbtn_0e_6_usa
"""
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker


class State(State):
    """
    Defines a state class that maps to the states table
    Attribute:
        id - Unique identification number for each entry
        name - The name of the state
    Method:
        __str__ - Print the object with representation <id>: <name>
    """
    def __str__(self):
        return f"{self.id}: {self.name}"


if __name__ == '__main__':

    mysqldb_info = {
        'drivername': 'mysql',
        'username': argv[1],
        'password': argv[2],
        'host': 'localhost',
        'database': argv[3]
    }
    # create multiple connections to the server
    engine = create_engine(str(URL.create(**mysqldb_info)), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    # Retrieve and delete State object where the name contains letter 'a'
    for state in session.query(State).filter(State.name.like('%a%')).all():
        session.delete(state)
    session.commit()

    session.close()
