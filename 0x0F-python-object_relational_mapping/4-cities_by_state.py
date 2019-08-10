#!/usr/bin/python3
"""Write a script that lists all cities from the database hbtn_0e_4_usa
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
        "SELECT cities.id, cities.name, states.name\
        FROM cities LEFT JOIN states\
        ON cities.state_id = states.id\
        ORDER BY cities.id ASC")
    for row in cur.fetchall():
        print (row)
    cur.close()
    database.close()
