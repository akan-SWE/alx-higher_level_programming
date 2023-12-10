#!/usr/bin/python3

def roman_to_int(roman_string):

    """ Converts Roman numerals to an integer

    :param roman_string: The string containing the roman numerals

    :return: Integer representing the roman numerals or None
    on failure
    """

    # roman_string is not a string or is None
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_dict = {'I': 1, 'X': 10, 'V': 5, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}

    r_string = roman_string.upper()  # capitalize

    prev, add = '', 0
    for num in r_string:

        num1, num2 = roman_dict.get(prev), roman_dict.get(num)

        # Handle subtractive principle
        if prev and num1 < num2:
            subtract = num2 - num1 - num1
            add += subtract
        else:
            add += num2  # normal addition

        prev = num
    return add
