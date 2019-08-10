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
        "SELECT cities.name FROM cities LEFT JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC", (sys.argv[4],))
    res = []    
    for row in cur.fetchall():
        res.append(row[0])
    res = ", ".join(res)
    print (res)
    cur.close()
    database.close()

