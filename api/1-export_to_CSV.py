import requests
import csv
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

    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todos:
            # Format TASK_COMPLETED_STATUS as "Completed" or "Not Completed"
            task_completed_status = "Completed" if task['completed'] else "Not Completed"
            csv_writer.writerow([user['id'], user['username'], task_completed_status, task['title']])

    print(f"CSV file '{csv_filename}' has been created with the employee's TODO list.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        export_employee_todo_to_csv(employee_id)
