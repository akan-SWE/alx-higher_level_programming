#!/usr/bin/python3

r, indicator = 0, 0
for x in range(0, 26):

    # Switch between lowercase and uppercase
    if not r:
        r = chr(122)
    elif not indicator:
        r = chr(ord(r) - 32 - 1)
        indicator = 1
    elif indicator:
        r = chr(ord(r) + 32 - 1)
        indicator = 0

    print('{}'.format(r), end='')  # output current character
