#!/usr/bin/python3

"""
Module: 11-model_state_insert

Adds the State object “Louisiana” to the database hbtn_0e_6_usa
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

    # create the State object
    state = State(name='Louisiana')

    # add object to the table and commit changes
    session.add(state)
    session.commit()

    print(state.id)

    session.close()  # end connection
