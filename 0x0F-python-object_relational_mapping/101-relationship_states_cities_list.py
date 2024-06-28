#!/usr/bin/python3
"""
Module: 101-relationship_states_cities_list

Lists all State objects, and corresponding City objects, contained in the
database hbtn_0e_101_usa
"""
from sys import argv
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

if __name__ == '__main__':

    mysqldb_info = {
        'drivername': 'mysql',
        'username': argv[1],
        'password': argv[2],
        'host': 'localhost',
        'database': argv[3]
    }

    engine = create_engine(str(URL.create(**mysqldb_info)), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)  # generate a session
    session = Session()  # create a new session

    for state in session.query(State).order_by(State.id).all():
        print(f'{state.id}: {state.name}')
        state.cities.sort(key=lambda c: c.id)  # sort cities list by city.id
        for city in state.cities:
            print(f'    {city.id}: {city.name}')

    session.close()  # end current session
