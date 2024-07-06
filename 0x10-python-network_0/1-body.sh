#!/bin/bash
# The Bash script takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -f -s -L "$1"
