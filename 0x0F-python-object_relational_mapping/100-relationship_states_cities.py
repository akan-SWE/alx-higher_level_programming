#!/usr/bin/python3
"""
Module: 100-relationship_states_cities

Creates the State “California” with the City “San Francisco” from the
database hbtn_0e_100_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':

    mysqldb_info = {
        'drivername': 'mysql',
        'username': argv[1],
        'password': argv[2],
        'host': 'localhost',
        'database': argv[3]
    }

    engine = create_engine(str(URL.create(**mysqldb_info)), pool_pre_ping=True)

    Base.metadata.create_all(bind=engine)  # create the table and columns

    Session = sessionmaker(bind=engine)  # generate a session
    session = Session()  # create a new session

    # create new State object
    state = State(name="California")
    session.add(state)
    session.commit()
    # create new City object
    city = City(name="San Francisco", state_id=state.id)
    session.add(city)
    session.commit()

    session.close()  # end current session
