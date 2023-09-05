#!/usr/bin/python3
"""
Sends a GET request to a URL, displays
the response body, and handles HTTP status codes.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
