#!/usr/bin/python3
"""
Module: 0-select_states

The script lists all states from the database hbtn_0e_0_usa
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


def list_all_states(cur: Cursor) -> None:
    """Retrieves all state names in the table"""
    cur.execute("SELECT * FROM states")
    for row in cur.fetchall():
        print(row)


def main(argv: list) -> None:
    """Entry point"""
    args = extract_args(argv)
    db = connect(*args)
    cursor = db.cursor()
    list_all_states(cursor)
    # end connections
    cursor.close()
    db.close()


if __name__ == '__main__':
    main(sys.argv)
