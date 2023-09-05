#!/usr/bin/python3
"""
Sends a POST request with an email parameter and displays the response body
"""

import urllib.request
import urllib.parse
import sys

if len(sys.argv) == 3:
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
