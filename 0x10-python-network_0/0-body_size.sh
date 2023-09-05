#!/bin/bash
# Send a GET request to the URL and write the response to a temporary file
curl -sI "$1" | grep -i Content-Length | awk '{print $2}' || echo 0

