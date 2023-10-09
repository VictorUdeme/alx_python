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
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for task in todos:
            # Format TASK_COMPLETED_STATUS as "Completed" or "Not Completed"
            task_completed_status = "Completed" if task['completed'] else "Not Completed"
            writer.writerow({"USER_ID": employee_id, "USERNAME": user['username'], "TASK_COMPLETED_STATUS": task_completed_status, "TASK_TITLE": task['title']})

if __name__ == "__main__":
    export_employee_todo_to_csv(int(sys.argv[1]))
