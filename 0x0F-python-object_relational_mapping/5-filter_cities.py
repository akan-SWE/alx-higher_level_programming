#!/usr/bin/python3
"""
Module: 3-my_safe_filter_states
List all cities of the state using the database hbtn_0e_0_usa while also
handling MYSQL injections.
"""
from MySQLdb.cursors import Cursor
import MySQLdb
import sys


def extract_args(args: list) -> tuple:
    """Extract arguments needed from command line"""
    return args[1], args[2], args[3], args[4]


def connect(name: str, passwd: str, database: str) -> MySQLdb.Connection:
    """Connect to the existing database"""
    return MySQLdb.connect(host='localhost', user=name, passwd=passwd,
                           port=3306, db=database)


def list_matching_states(cur: Cursor, state_name: str) -> None:
    """List all cities in a state"""
    statement = ("SELECT c.name "
                 "FROM cities c JOIN states s ON c.state_id = s.id "
                 "WHERE s.name = %s ORDER BY c.id")
    cur.execute(statement, (state_name,))
    print(", ".join(str(row[0]) for row in cur.fetchall()))


def main(argv: list) -> None:
    """Main logic - It extracts arguments , connects to the database,
    execute the query and close connections
    """
    args = extract_args(argv)
    db = connect(*args[:3])
    cursor = db.cursor()
    list_matching_states(cursor, args[3])
    # end connections
    cursor.close()
    db.close()


if __name__ == '__main__':
    main(sys.argv)
