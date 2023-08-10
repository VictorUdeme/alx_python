"""
import module(requests and sys)
"""
import requests
import sys

def get_request_id(url):
    """
    Gets the value of the X-Request-Id header
    from the response to the given URL.
    """
    response = requests.get(url)
    return response.headers['X-Request-Id']

if __name__ == '__main__':
    ur1 = sys.argv[1]
    request_id = get_request_id(ur1)
    print(request_id)
    
