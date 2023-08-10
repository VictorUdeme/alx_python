"""
imports requests_package
"""
import requests
def fetch_status():
    """
    defines fetch_status
    """
    response = requests.get('https://alu-intranet.hbtn.io/status')
    if response.status_code == 200:
        data = response.json()  # Assuming the response content is in JSON format
        formatted_response = f'Body respons: \n\t- type: {type(data)}\n\t- content: {data}'
        return formatted_response
    else:
        raise Exception('Failed to fetch status code')
    
"""Calling the function"""
try:
    status = fetch_status()
    print(status)
except Exception as e:
    print("An error occurred:", e)