#!/usr/bin/python3
"""
Sends a request to a URL and displays the X-Request-Id variable from the header
"""

import urllib.request
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        headers = response.info()
        x_request_id = headers.get('X-Request-Id')
        print(x_request_id)
