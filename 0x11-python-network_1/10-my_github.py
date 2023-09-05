#!/usr/bin/python3
"""
Displays your GitHub id using Basic Authentication with a personal access token.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./github_id.py <username> <access_token>")
        sys.exit(1)

    username = sys.argv[1]
    access_token = sys.argv[2]

    url = f"https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, access_token))

        if response.status_code == 200:
            user_data = response.json()
            print("Your GitHub ID is:", user_data["id"])
        else:
            print("Error:", response.status_code, response.text)
    except requests.RequestException as e:
        print("Request Error:", e)
    except KeyError:
        print("Invalid JSON response")
