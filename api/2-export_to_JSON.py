"""
This module provides a function to fetch an employee's TODO list from a REST API and export it to a JSON file.
"""

import json
import requests
import sys

def export_employee_todo_to_json(employee_id):
    """
    The function fetches the employee's details and their TODO list from the API, and writes them to a JSON file.
    The JSON file is named after the employee's ID and contains the following format:
    { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ...]}

    Args:
    employee_id (int): The ID of the employee.
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    response = requests.get(user_url)
    user = response.json()
    response = requests.get(todos_url)
    todos = response.json()

    tasks = []
    for task in todos:
        tasks.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": user['username']
        })

    with open(f"{employee_id}.json", "w") as jsonfile:
        json.dump({employee_id: tasks}, jsonfile)
        print("Correct USER_ID: OK")

if __name__ == "__main__":
    export_employee_todo_to_json(int(sys.argv[1]))