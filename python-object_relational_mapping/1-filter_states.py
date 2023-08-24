#!/usr/bin/python3
"""
Lists all states with a name starting 
with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(user=username,
                         passwd=password,
                         db=db_name,
                         host="localhost",
                         port=3306)
    cur = db.cursor()

    query = ("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
             "ORDER BY id ASC")
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()

    db.close()


