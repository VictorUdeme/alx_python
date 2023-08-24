#!/usr/bin/python3
"""
List all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                JOIN states ON cities.state_id = states.id WHERE states.name=%s\
                ORDER BY cities.id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    cities = []
    for row in rows:
        cities.append(row[1])
    print(", ".join(cities))
    cur.close()
    db.close()
