"""
imported requests module
"""


import requests
import sys

def search_user(letter):
    url = "http://0.0.0.0:5000/search_user"
    params = {"q": letter}
    response = requests.post(url, data=params)
    
    try:
        json_data = response.json()
        
        if json_data:
            user_info = f"[{json_data['id']}] {json_data['name']}"
            print(user_info)
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    
    search_user(letter)
