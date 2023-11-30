#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Get the last digit
if number < 0:
    last_digit = (-number % 10) * -1  # last digit is negative
else:
    last_digit = number % 10  # last digit is positive

if not last_digit:
    print(f'Last digit of {number} is {last_digit} and is 0')
elif last_digit > 5:
    print(f'Last digit of {number} is {last_digit} and is greater than 5')
else:
    print(f'Last digit of {number} is {last_digit} '
          f'and is less than 6 and not 0')
