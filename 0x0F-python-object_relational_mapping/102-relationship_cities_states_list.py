#!/usr/bin/python3
"""
Module: 102-relationship_cities_states_list

Lists all City objects from the database hbtn_0e_101_usa
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

    # list all City object and state linked to the City object
    for city in session.query(City).order_by(City.id).all():
        print(f'{city.id}: {city.name} -> {city.state.name}')

    session.close()  # end current session
