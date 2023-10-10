import csv
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    api_request = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    api_request1 = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    pjson = api_request.json()
    pjson1 = api_request1.json()

    #export data to csv data
    filename = "{}.csv".format(employee_id)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting = csv.QUOTE_ALL)
        for item in pjson1:
            user_id = employee_id
            username = pjson['username']
            task_completed_status = item['completed']
            task_title = item['title']
            writer.writerow([user_id, username, task_completed_status, task_title])