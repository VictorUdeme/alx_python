"""
importing module
"""


import requests

url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)

if response.status_code == 200:
    content = response.text
    print("[{}]".format(content))
    print("({} chars long)".format(len(content)))
else:
    print("Error:", response.status_code)
 
