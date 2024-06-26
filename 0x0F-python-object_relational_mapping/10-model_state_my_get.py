#!/usr/bin/python3

"""
Module: 10-model_state_my_get

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
                  'port': 3306,
                  'database': argv[3]
                  }
    # create multiple connections to the server
    engine = create_engine(str(URL.create(**mysql_info)), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)  # generate a session
    session = Session()

    query = session.query(State).filter(State.name == argv[4]).all()
    if query:
        for row in query:
            print(row.id)
    else:
        print('Not found')

    session.close()  # end connection
