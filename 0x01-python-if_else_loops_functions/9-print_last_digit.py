#!/usr/bin/python3


def print_last_digit(number):
    # ignore negative numbers
    if number < 0:
        number = -number

    last_digit = number % 10
    print(last_digit, end='')
    return last_digit
