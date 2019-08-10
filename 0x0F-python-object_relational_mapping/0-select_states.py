#!/usr/bin/python3
"""Selects all states and ids from table
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               charset="utf8",
                               user=argv[1],
                               passwd=argv[2],
                               db=argv[3])
    cur = database.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    for row in cur.fetchall():
        print (row)
    cur.close()
    database.close()
