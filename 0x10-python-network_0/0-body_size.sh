#!/bin/bash
# Send a GET request to the URL and write the response to a temporary file
curl -s "$1" | wc -c
