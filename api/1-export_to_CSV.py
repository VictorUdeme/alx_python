import csv
import requests
import sys


def get_employee_data(employee_id):
    """
    Fetches employee's TODO list progress and exports it to a CSV file.

    Args:
        employee_id (int): The ID of the employee to retrieve information for.
    """
    # Define the API endpoints
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    try:
        # Fetch employee data
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()

        # Fetch TODO list data
        todo_response = requests.get(todo_url)
        todo_list = todo_response.json()

        # Create a CSV file for the employee
        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            
            # Write the CSV header
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            # Write the TODO list data to the CSV
            for task in todo_list:
                csv_writer.writerow([employee_id, employee_data['username'], task['completed'], task['title']])

        print(f"CSV file '{csv_filename}' has been created with TODO list data for Employee {employee_data['name']}.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)
