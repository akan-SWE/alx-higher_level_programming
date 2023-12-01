#!/usr/bin/python3

def remove_char_at(str, n):
    copy = ''
    i = 0
    for char in str:
        if i == n:  # remove character at this index
            copy += ''
            i += 1
            continue

        copy += char  # Adds characters to copy for each iteration
        i += 1
    return copy
