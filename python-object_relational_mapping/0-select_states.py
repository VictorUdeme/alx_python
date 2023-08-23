import MySQLdb

def main():
    """Lists all states from the database hbtn_0e_0_usa."""

    username = input("Enter MySQL username: ")
    password = input("Enter MySQL password: ")
    database = input("Enter MySQL database name: ")

    connection = MySQLdb.connect(host="localhost", port=3306, user=username, password=password, db=database)
    cursor = connection.cursor()

    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    for row in cursor:
        print(row)

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
