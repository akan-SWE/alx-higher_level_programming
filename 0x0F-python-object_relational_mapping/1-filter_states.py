#!/usr/bin/python3
"""
Module: 1-filter_states

The script lists all states from the database hbtn_0e_0_usa that
their name start with a capital 'N'
"""
import MySQLdb
import sys


def extract_args(args: list) -> tuple:
    """Exract arguments needed from command line"""
    return args[1], args[2], args[3]


def connect(name: str, passwd: str, database: str) -> MySQLdb.Connection:
    """Connect to the existing database"""
    return MySQLdb.connect(host='localhost', user=name, passwd=passwd,
                           port=3306, db=database)


def list_N_states(cur) -> None:
    """Retrieves all states that their name start with a capital N"""
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    for row in cur.fetchall():
        print(row)


def main(argv: list) -> None:
    """Main logic - It extracts arguments , connects to the database,
    execute the query and close connections
    """
    args = extract_args(argv)
    db = connect(*args)
    cursor = db.cursor()
    list_N_states(cursor)
    # end connections
    cursor.close()
    db.close()


if __name__ == '__main__':
    main(sys.argv)
