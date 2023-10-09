import requests

def get_employee_todo_progress(employee_id):
    """
    Retrieves information about a given employee's TODO list progress from the provided REST API.

    Parameters:
        employee_id (int): The ID of the employee to retrieve TODO list progress for.

    Returns:
        None

    Prints:
        The employee TODO list progress in the following format:
            Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
            (with EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, and TOTAL_NUMBER_OF_TASKS replaced by actual values)
        The titles of the completed tasks, with one tab and one space before each title.
    """
    # Endpoint URLs
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    
    # Get employee details
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data['name']
    
    # Get TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    # Count completed tasks
    completed_tasks = [task for task in todos_data if task['completed']]
    num_completed_tasks = len(completed_tasks)
    
    # Print employee TODO list progress
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{len(todos_data)}):")
    
    # Print titles of completed tasks
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    # Example usage: get_employee_todo_progress(1)
    get_employee_todo_progress(1)
