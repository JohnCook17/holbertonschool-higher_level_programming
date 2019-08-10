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
    cur.execute(
        "SELECT * FROM states WHERE name like %s ORDER BY id ASC",
        (sys.argv[4],))
    for row in cur.fetchall():
        print (row)
    database.close()
