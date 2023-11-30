#!/usr/bin/python3

def uppercase(input_string):
    result = ''
    for char in input_string:
        if 'a' <= char <= 'z':  # Check if the character is lowercase
            result += chr(ord(char) - 32)  # Convert lowercase to uppercase
        else:
            result += char  # Keep non-alphabetic characters unchanged
    print('{}'.format(result))
