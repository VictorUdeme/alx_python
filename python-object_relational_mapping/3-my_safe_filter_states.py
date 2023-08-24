"""
Displays all values in the states table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=db_name,
        host="localhost",
        port=3306
    )
    
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))
    
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
