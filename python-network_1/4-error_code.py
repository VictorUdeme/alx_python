"""
module-code_erro
"""


import requests
import sys

def main():
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)

if __name__ == "__main__":
    main()

