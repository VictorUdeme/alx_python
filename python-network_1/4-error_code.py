"""
module-code_erro
"""


import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    
    try:
        response = requests.get(url)
        print(response.text)
        
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    
if __name__ == "__main__":
    main()

