"""
modules used:
requests and sys
"""


import requests
import sys

def get_github_id(username, access_token):
    """
    Get github username and token
    """
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, access_token))

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get("id")
        print(user_id)

    else:
        print("None")
       


if __name__ == '__main__':
    username = sys.argv[1]
    access_token = sys.argv[2]
    get_github_id(username, access_token)