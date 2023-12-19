#!/usr/bin/python3

def safe_print_division(a, b):

    try:
        result = a / b
    except ZeroDivisionError:
        result = None  # cannot divide by zero
    finally:
        # always execute this code
        print('Inside result: {}'.format(result))
        return result
