#!/usr/bin/python3
"""
Sends a POST request with an email parameter
to a URL and displays the response body.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print(response.text)
