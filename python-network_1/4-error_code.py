"""
module-code_erro
"""


import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    
    try:
        response = requests.get(url)
        print("Response body:")
        print(response.text)
        
        if response.status_code >= 400:
            print("Error code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main() 

