"""
import module(requests and sys)
"""
import requests
import sys

def get_x_request_id(url):
    """
    Gets the value of the X-Request-Id header
    from the response to the given URL.
    """
    response = requests.get(url)
    return response.headers['X-Request-Id']
