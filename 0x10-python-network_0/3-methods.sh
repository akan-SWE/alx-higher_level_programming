#!/bin/bash
# The Bash script takes in a URL and displays all HTTP methods the server will accept
curl -s -I -X OPTIONS "$1" | grep -w "Allow:" | cut -c 8-
