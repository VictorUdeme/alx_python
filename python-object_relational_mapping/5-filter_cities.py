import MySQLdb

def list_cities_by_state(username, password, database, state):
  """
  Lists all cities of the specified state.

  Args:
    username: The MySQL username.
    password: The MySQL password.
    database: The MySQL database name.
    state: The name of the state.

  Returns:
    A list of cities.
  """

  connection = MySQLdb.connect(host="localhost", port=3306, user=username, password=password, database=database)
  cursor = connection.cursor()

  query = "SELECT name FROM cities WHERE state = %s ORDER BY id ASC"
  cursor.execute(query, (state,))

  cities = []
  for row in cursor:
    cities.append(row[0])

  connection.close()

  return cities

if __name__ == "__main__":
  # Get the arguments
  username = input("Enter MySQL username: ")
  password = input("Enter MySQL password: ")
  database = input("Enter MySQL database name: ")
  state = input("Enter state name: ")

  # List the cities
  cities = list_cities_by_state(username, password, database, state)

  # Print the results
  print("The following cities are in the state of {}:".format(state))
  for city in cities:
    print(city)
