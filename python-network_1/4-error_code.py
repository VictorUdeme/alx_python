"""
module-code_erro
"""


import requests
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("Response Body:")
        print(response.text)
    else:
        print("Error:", response.status_code)

if __name__ == "__main__":
    main()


