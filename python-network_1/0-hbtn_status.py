"""
importing module
"""

import requests

url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)

if response.status_code == 200:
    data = response.text
    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data)
else:
    print("Failed to fetch data from the URL. Status code:", response.status_code)


  