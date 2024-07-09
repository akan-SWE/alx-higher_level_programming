#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and
displays the body of the response.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    response = requests.get(argv[1])
    status_code = response.status_code
    print(f'Error code: {status_code}' if status_code > 399 else response.text)
