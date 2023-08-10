"""
imports requests_package
"""
import requests
def fetch_status():
    """
    defines fetch_status
    """
    response = requests.get('https://alu-intranet.hbtn.io/status')
    return response.text