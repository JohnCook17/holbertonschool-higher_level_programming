#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import MySQLdb

    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=sys.argv[1],
                               passwd=sys.argv[2],
                               db=sys.argv[3])
    cur = database.cursor()
    cur.execute("SELECT states.id, states.name FROM states WHERE name like 'N%' ORDER BY id ASC")
    for row in cur.fetchall():
        print (row)
    database.close()
