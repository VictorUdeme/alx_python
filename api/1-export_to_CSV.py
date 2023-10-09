import csv
import requests
import sys

def export_employee_todo_to_csv(employee_id):
    """
    The function fetches the employee's details and their TODO list from the API, and writes them to a CSV file.
    The CSV file is named after the employee's ID and contains the following columns:
    USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE

    Args:
    employee_id (int): The ID of the employee.
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    response = requests.get(user_url)
    user = response.json()
    response = requests.get(todos_url)
    todos = response.json()

    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            # Convert the boolean value to a string
            completed_status = str(task['completed']).lower()
            writer.writerow([employee_id, user['username'], completed_status, task['title']])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    export_employee_todo_to_csv(int(sys.argv[1]))
