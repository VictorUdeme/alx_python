"""
module-code_erro
"""


import requests
import sys

def send_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text)
        else:
            print("Error code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

# Replace 'url_here' with the actual URL you want to send a request to
send_request('url_here')
