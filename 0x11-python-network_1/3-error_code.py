#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""

if __name__ == '__main__':
    from sys import argv
    from urllib import request, error

    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as code:
        print('Error code:', code.status)
