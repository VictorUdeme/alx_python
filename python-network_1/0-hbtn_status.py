"""
importing module
"""

import requests

request = requests.get("https://alu-intranet.hbtn.io/status")
requests.status(request)
  