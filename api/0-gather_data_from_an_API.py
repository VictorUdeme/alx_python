"""
This module provides a function to fetch and display the progress of an employee's TODO list
from a REST API. The employee is specified by their ID.
"""


import requests
import sys

def get_employee_data(employee_id):
    """
    Fetches employee's TODO list progress and displays it on the standard output.

    Args:
        employee_id (int): The ID of the employee to retrieve information for.

    Returns:
        None
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

        # Calculate TODO list progress
        total_tasks = len(todo_list)
        completed_tasks = sum(1 for task in todo_list if task['completed'])

        # Display the progress
        print(f"Employee {employee_data['name']} is done with tasks ({completed_tasks}/{total_tasks}):")
        for task in todo_list:
            if task['completed']:
                print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)
