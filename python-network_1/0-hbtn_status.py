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
        return response.text
    else:
        raise Exception('Failed to fetch status code')
    