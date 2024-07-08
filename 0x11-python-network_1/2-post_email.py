#!/usr/bin/python3
"""
This script takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

if __name__ == '__main__':
    from sys import argv
    from urllib import request, parse
    # converts string to bytes
    email = parse.urlencode({'email': argv[2]}).encode()
    # send POST request and display the body of the response
    with request.urlopen(argv[1], email) as response:
        print(response.read().decode('utf-8'))
