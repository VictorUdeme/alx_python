"""
importing module
"""

import requests

response = requests.get('https://alu-intranet.hbtn.io/status')

if response.status_code == 200:
    for line in response.text.splitlines():
        print(f"\t- {line}")
else:
    print(f"An error occurred: {response.status_code}")



  