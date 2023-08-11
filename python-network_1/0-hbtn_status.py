"""
importing module
"""

import requests

url = "https://alu-intranet.hbtn.io/status"
request = requests.get(url)

if request.status_code == 200:
    data = request.text
    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data)
else:
    print("Failed to fetch data from the URL. Status code:", request.status_code)


  