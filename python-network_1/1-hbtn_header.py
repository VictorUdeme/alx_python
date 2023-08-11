"""
import module(requests and sys)
"""


import requests
import sys

if len(sys.argv) < 2:
    print("Usage: python script_name.py <URL>")
    sys.exit(1)

url = sys.argv[1]
response = requests.get(url)

if response.status_code == 200:
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print("X-Request-Id:", x_request_id)
    else:
        print("X-Request-Id not found in response headers.")
else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")


    
