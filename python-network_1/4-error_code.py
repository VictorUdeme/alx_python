"""
module-code_erro
"""


import requests
import sys

def get_url_content(url):
    response = requests.get(url)
    status_code = response.status_code

    if status_code >= 400:
        print(f"Error code: {status_code}")
    else:
        print(response.text)
