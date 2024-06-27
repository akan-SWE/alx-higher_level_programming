#!/usr/bin/python3

"""
Module: 14-model_city_fetch_by_state

Prints all City objects from the database hbtn_0e_14_usa
"""
from sys import argv
from model_city import City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

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

    # Retrieve City objects and their State
    records = (session.query(State, City)
               .filter(State.id == City.state_id)
               .order_by(City.id).all())

    for record in records:
        print(f'{record[0].name}: ({record[1].id}) {record[1].name}')

    session.close()  # end session
