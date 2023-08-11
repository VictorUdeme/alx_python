"""
imports module
"""
import requests

url = 'https://alu-intranet.hbtn.io/status'

response = requests.get(url)

if response.status_code == 200:
    print('Body of the response:')
    print('-' * 10)
    print(response.text)
else:
    print('Error fetching the status page')
    print(response.status_code)
