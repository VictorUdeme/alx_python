"""
imports requests_package
"""


import requests

def fetch_and_display_status(url):
    """
    Fetches the status from a given URL using the requests package.
    
    Args:
        url (str): The URL to fetch the status from.
        
    Returns:
        None
        
    Prints:
        The type and content of the response in a specific format.
    """
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("Body response:")
        print("\t- type:", type(data))
        print("\t- content:", data)
    else:
        print("Failed to fetch the URL. Status code:", response.status_code)

# URL to fetch the status from
url = "https://alu-intranet.hbtn.io/status"

# Fetch and display the status
fetch_and_display_status(url)

