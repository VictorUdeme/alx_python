"""
This module provides a function to fetch and display the progress of an employee's TODO list
from a REST API and export the data in CSV format. The employee is specified by their ID.
"""

import requests
import csv
import sys

def get_employee_todo_progress_and_export_csv(employee_id):
    """
    The function fetches the employee's details and their TODO list from the API, filters the tasks
    that are marked as completed, and prints the progress in the following format:

    Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    TASK_TITLE

    It also exports the data in CSV format with the following columns:
    - USER_ID
    - USERNAME
    - TASK_COMPLETED_STATUS
    - TASK_TITLE

    Args:
    employee_id (int): The ID of the employee.
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    response = requests.get(user_url)
    user = response.json()
    response = requests.get(todos_url)
    todos = response.json()

    done_tasks = [task for task in todos if task['completed']]

    # Display employee TODO list progress
    print(f"Employee {user['name']} is done with tasks({len(done_tasks)}/{len(todos)}):")
    for task in done_tasks:
        print(f"\t {task['title']}")

    # Export data to CSV file
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in done_tasks:
            csv_writer.writerow([user['id'], user['username'], "Completed", task['title']])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress_and_export_csv(employee_id)
