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

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        get_url_content(url)
    else:
        print("Please provide a URL as an argument.")
