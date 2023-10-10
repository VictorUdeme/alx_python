import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    
    # Make API requests to retrieve user and tasks data
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    tasks_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")

    if user_response.status_code != 200 or tasks_response.status_code != 200:
        print("Error: Failed to retrieve data from the API.")
        sys.exit(1)

    user_data = user_response.json()
    tasks_data = tasks_response.json()

    # Create a CSV file and write the data
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for task in tasks_data:
            user_id = employee_id
            username = user_data['username']
            task_completed_status = task['completed']
            task_title = task['title']
            writer.writerow([user_id, username, task_completed_status, task_title])

    print(f"CSV file '{filename}' has been created.")
