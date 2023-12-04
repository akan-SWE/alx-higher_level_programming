#!/usr/bin/python3

char_code, indicator = 0, 0
for x in range(0, 26):

    # Switch between lowercase and uppercase
    if not char_code:
        char_code = chr(122)  # Starting point from 'z'
    elif not indicator:
        char_code = chr(ord(char_code) - 32 - 1)
        indicator = 1
    elif indicator:
        char_code = chr(ord(char_code) + 32 - 1)
        indicator = 0

    print('{}'.format(char_code), end='')  # Output current character
