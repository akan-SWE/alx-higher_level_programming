#!/usr/bin/python3
"""
This script fetches a response from the server at
https://alx-intranet.hbtn.io/status.
"""

if __name__ == '__main__':
    import requests

    response_body = requests.get('https://alx-intranet.hbtn.io/status').text

    print(f'Body response:\n'
          f'\t- type: {type(response_body)}\n\t- content: {response_body}')
