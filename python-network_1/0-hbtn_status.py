import requests

"""
importing module
"""

response = requests.get('https://alu-intranet.hbtn.io/status')

if response.status_code == 200:
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
else:
    print(f"An error occurred: {response.status_code}")
