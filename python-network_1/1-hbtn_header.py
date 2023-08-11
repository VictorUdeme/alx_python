"""
import module(requests and sys)
"""


import requests
import sys

url = sys.argv[1]

response = requests.get(url)
headers = response.headers

if 'X-Request-Id' in headers:
    x_request_id = headers['X-Request-Id']
    print(x_request_id)
else:
    print("X-Request-Id not found in response headers.")
    
