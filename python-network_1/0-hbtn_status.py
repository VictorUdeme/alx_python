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
        formatted_response = f'Body respons: \n\t- type: {type(response.text)}\n\t- content: {response.text}'
        return formatted_response
    else:
        raise Exception('Failed to fetch status code')
