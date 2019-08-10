#!/usr/bin/python3
"""Write a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa where name
matches the argument.
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
    cur.execute(
        "SELECT * FROM states WHERE name like BINARY '{}' ORDER BY id ASC"
        .format(sys.argv[4]))
    for row in cur.fetchall():
        print (row)
    cur.close()
    database.close()
