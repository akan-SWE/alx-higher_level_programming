#!/usr/bin/python3
"""
This script fetches a response from the server at
https://alx-intranet.hbtn.io/status.
"""

if __name__ == '__main__':
    from urllib import request

    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        utf8_content = content.decode('utf-8')
        print('Body response:')
        print(f'\t- type: {type(content)}\n\t- content: {content}'
              f'\n\t- utf8 content: {utf8_content}')
