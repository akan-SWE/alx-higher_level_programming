#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    q = '' if len(argv) == 1 else argv[1]

    response = requests.post('http://0.0.0.0:5000/search_user', {'q': q})
    try:
        data = response.json()
        print(f"[{data.get('id')}] {data.get('name')}" if data else "No result")
    except KeyError:
        print('Not a valid JSON')
