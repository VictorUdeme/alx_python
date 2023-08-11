"""
module-code_erro
"""


import requests
import sys

def fetch_and_display(url):
    response = requests.get(url)
    
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    fetch_and_display(url)




