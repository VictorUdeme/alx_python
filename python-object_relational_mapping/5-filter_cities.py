import sys
import MySQLdb

if __name__ == '__main__':
    
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database_name)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to retrieve all cities of the given state
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                    JOIN states ON cities.state_id = states.id WHERE states.name = %s \
                    ORDER BY cities.id ASC", (state_name,))

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Print the results in the specified format
    print('\n'.join([f'{row[0]}: {row[1]} ({row[2]})' for row in rows]))

    # Close the cursor and database connections
    cursor.close()
    db.close()
