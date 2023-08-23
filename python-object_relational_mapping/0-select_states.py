import mysql.connector

# Function to connect to the MySQL server
def connect_to_mysql(username, password, database):
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user=username,
            password=password,
            database=database
        )
        print("Connected to MySQL server successfully")
        return connection
    except mysql.connector.Error as error:
        print("Failed to connect to MySQL server: {}".format(error))
        return None

# Function to list all states from the database
def list_states(connection):
    if connection is None:
        return

    try:
        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute the SQL query to list all states
        query = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(query)

        # Fetch all the rows returned by the query
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

        # Close the cursor and connection
        cursor.close()
        connection.close()
    except mysql.connector.Error as error:
        print("Failed to execute the query: {}".format(error))

# Main function
def main():
    # Get the MySQL credentials from the user
    username = input("Enter MySQL username: ")
    password = input("Enter MySQL password: ")
    database = input("Enter database name: ")

    # Connect to the MySQL server
    connection = connect_to_mysql(username, password, database)

    # List all states from the database
    list_states(connection)

# Execute the main function
if __name__ == "__main__":
    main()
