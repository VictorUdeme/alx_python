"""
imports requests_package
"""
import requests

url = 'https://alu-intranet.hbtn.io/status'
response = requests.get(url)

if response.status_code == 200:
    print("Body response")
    print("\t- type: <class 'str'>")
    print("\t- content: OK")
else:
    print(f"Error: {response.status_code}")
   
