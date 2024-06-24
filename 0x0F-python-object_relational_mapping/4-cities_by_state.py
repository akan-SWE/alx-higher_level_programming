#!/usr/bin/python3
"""
Module: 4-cities_by_state

List all cities from the database hbtn_0e_4_usa
"""
from MySQLdb.cursors import Cursor
import MySQLdb
import sys


def extract_args(args: list) -> tuple:
    """Extract arguments needed from command line"""
    return args[1], args[2], args[3]


def connect(name: str, passwd: str, database: str) -> MySQLdb.Connection:
    """Connect to the existing database"""
    return MySQLdb.connect(host='localhost', user=name, passwd=passwd,
                           port=3306, db=database)


def list_all_cities(cur: Cursor) -> None:
    """Retrives all cities along with their state"""
    statement = ("SELECT c.id, c.name, s.name "
                 "FROM cities c JOIN states s "
                 "ON state_id = s.id ORDER BY c.id")
    cur.execute(statement)
    for row in cur.fetchall():
        print(row)


def main(argv: list) -> None:
    """Main logic - It extracts arguments , connects to the database,
    execute the query and close connections
    """
    args = extract_args(argv)
    db = connect(*args)
    cursor = db.cursor()
    list_all_cities(cursor)
    # end connections
    cursor.close()
    db.close()


if __name__ == '__main__':
    main(sys.argv)
