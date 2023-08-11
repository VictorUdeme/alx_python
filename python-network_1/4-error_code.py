"""
module-code_erro
"""


import requests
import sys

url = input("Enter a URL: ").strip()

if not url:
    print("Error: URL is required")
    sys.exit()

response = requests.get(url)

if response.status_code >= 400:
    print(f"Error code: {response.status_code}")
    sys.exit()

print(response.text)


