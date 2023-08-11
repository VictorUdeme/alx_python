"""
module-code_erro
"""


import requests
import sys

def main():
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print('Error code: {}'.format(response.status_code))
    else:
        print('Body of the response:')
        print('-' * 10)
        print(response.text)

if __name__ == '__main__':
    main()
