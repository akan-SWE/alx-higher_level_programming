#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""

if __name__ == '__main__':
    from sys import argv
    from urllib import request

    url = argv[1]
    with request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
