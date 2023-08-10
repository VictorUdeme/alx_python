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
    response = get_x_request_id
    x_request_id = response.header.get('X-Request-Id')
    return x_request_id

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("Usage: python script_name.py <URL>")
    else:
        ur1 = sys.argv[1]
        x_request_id = get_x_request_id(ur1)

        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id not found in response headers")


