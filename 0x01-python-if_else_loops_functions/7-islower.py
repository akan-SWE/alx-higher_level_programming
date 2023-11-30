#!/usr/bin/python3

def islower(c):
    alphabet = chr(ord(c))  # convert to character
    low, high = alphabet >= 'a', alphabet <= 'z'  # range from a - z
    if low and high:
        return True

    return False  # uppercase
