#!/usr/bin/python3
"""
Module: 7-model_state_fetch_all

The script lists all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
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

    mysql_info = {'drivername': 'mysql',
                  'username': argv[1],
                  'password': argv[2],
                  'host': 'localhost',
                  'database': argv[3]
                  }
    # create multiple connections to the server
    engine = create_engine(str(URL.create(**mysql_info)), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)  # generate a session
    session = Session()

    # retrieve all State object sorted in ascending order by states.id
    for row in session.query(State).order_by(State.id).all():
        print(row)

    session.close()  # end session
