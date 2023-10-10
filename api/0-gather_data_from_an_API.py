"""
This module provides a function to fetch and display the progress of an employee's TODO list
from a REST API. The employee is specified by their ID.
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    The function fetches the employee's details and their TODO list from the API, filters the tasks
    that are marked as completed, and prints the progress in the following format:

    Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    TASK_TITLE

    where:
    EMPLOYEE_NAME: name of the employee
    NUMBER_OF_DONE_TASKS: number of completed tasks
    TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
    TASK_TITLE: title of the completed task

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
    total_tasks = len(todos)

    print(f"Employee {user['name']} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    get_employee_todo_progress(int(sys.argv[1]))