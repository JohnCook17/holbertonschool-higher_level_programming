#!/usr/bin/python3

import sys
import MySQLdb


database = MySQLdb.connect(host="localhost",
                     port=3306,
                     user=sys.argv[1],
                     passwd=sys.argv[2],
                     db=sys.argv[3])
cur = database.cursor()
cur.execute("SELECT * FROM states")
for row in cur.fetchall():
    print (row)
database.close()
