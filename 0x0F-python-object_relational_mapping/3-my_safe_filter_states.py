#!/usr/bin/python3
"""
Module: 3-my_safe_filter_states
displays all values in the states table of hbtn_0e_0_usa where name
matches the argument and is safe from MYSQL injections.
"""
from MySQLdb.cursors import Cursor
import MySQLdb
import sys


def extract_args(args: list) -> tuple:
    """Exract arguments needed from command line"""
    return args[1], args[2], args[3], args[4]


def connect(name: str, passwd: str, database: str) -> MySQLdb.Connection:
    """Connect to the existing database"""
    return MySQLdb.connect(host='localhost', user=name, passwd=passwd,
                           port=3306, db=database)


def list_matching_states(cur: Cursor, state_name: str) -> None:
    """Retrieves all states that their name start with a capital N"""
    statement = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cur.execute(statement, (state_name,))
    for row in cur.fetchall():
        print(row)


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
