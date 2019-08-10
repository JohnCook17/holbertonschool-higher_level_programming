#!/usr/bin/python3
"""Selects all states and ids from table
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=argv[1],
                               passwd=argv[2],
                               db=argv[3])
    cur = database.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    for row in cur.fetchall():
        print (row)
    cur.close()
    database.close()
