#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    try:
        response = requests.post(url, data=data)
        response_data = response.json()

        if response_data:
            print("[{}] {}".format(response_data.get(
                "id"), response_data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except Exception as e:
        print("Error:", e)
