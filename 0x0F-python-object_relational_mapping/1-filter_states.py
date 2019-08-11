#!/usr/bin/python3
"""Write a script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa:
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=sys.argv[1],
                               passwd=sys.argv[2],
                               db=sys.argv[3])
    cur = database.cursor()
    cur.execute("SELECT states.id, states.name FROM states\
                WHERE name like BINARY 'N%' ORDER BY states.id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    database.close()
