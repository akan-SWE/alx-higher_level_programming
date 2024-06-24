#!/usr/bin/env python3
from MySQLdb.cursors import Cursor
import MySQLdb
import sys


def extract_args(args: list) -> tuple:
    return args[1], args[2], args[3], args[4]


def connect(name: str, passwd: str, database: str) -> MySQLdb.Connection:
    return MySQLdb.connect(host='localhost', user=name, passwd=passwd,
                           port=3306, db=database)


def list_matching_states(cur: Cursor, state_name: str) -> None:
    cur.execute("SELECT * FROM states "
                "WHERE name = '{}' ORDER BY id".format(state_name))
    for row in cur.fetchall():
        print(row)


def main(argv: list) -> None:
    args = extract_args(argv)
    db = connect(*args[:3])
    cursor = db.cursor()
    list_matching_states(cursor, args[3])
    # end connections
    cursor.close()
    db.close()


if __name__ == '__main__':
    main(sys.argv)
