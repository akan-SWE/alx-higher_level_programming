#!/usr/bin/python3
"""
This script takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    print(requests.post(argv[1], data={'email': argv[2]}).text)
