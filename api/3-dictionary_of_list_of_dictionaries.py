import json
import requests

def export_all_employee_todo_to_json():
    """
    Fetch all employees' TODO list from a REST API and export it to a JSON file.

    The function fetches the details and TODO lists of all employees from the API, and writes them to a JSON file.
    The JSON file is named "todo_all_employees.json" and contains the following format:
    { "USER_ID": [{"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ...], ...}
    """
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    response = requests.get(users_url)
    users = response.json()

    all_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        response = requests.get(todos_url, params={'userId': user_id})
        todos = response.json()

        tasks = []
        for task in todos:
            tasks.append({
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            })

        all_tasks[user_id] = tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)

if __name__ == "__main__":
    export_all_employee_todo_to_json()