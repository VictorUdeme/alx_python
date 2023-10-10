import csv
import requests
import sys

def user_info(employee_id):
    """
    Fetches employee's TODO list progress, exports it to a CSV file, and then reads and displays the information.

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

        print("Number of tasks in CSV: OK")

        # Now, let's read and display the information from the CSV file
        with open(csv_filename, 'r') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                user_id, username, completed, task_title = row
                print(f"User ID: {user_id}, Username: {username}")
                print(f"Task Completed Status: {completed}")
                print(f"Task Title: {task_title}\n")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_info(employee_id)
