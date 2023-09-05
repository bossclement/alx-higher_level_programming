#!/usr/bin/python3
"""
Lists 10 most recent commits of a GitHub repository.
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <owner> <repository>".format(sys.argv[0]))
        sys.exit(1)

    owner = sys.argv[1]
    repository = sys.argv[2]

    github_api_url = "https://api.github.com/repos/{}/{}/commits".format(
        owner, repository)

    response = requests.get(github_api_url)
    commit_data = response.json()

    try:
        for i in range(10):
            commit = commit_data[i]
            sha = commit.get("sha")
            author_name = commit.get("commit").get("author").get("name")
            print("{}: {}".format(sha, author_name))
    except IndexError:
        pass
