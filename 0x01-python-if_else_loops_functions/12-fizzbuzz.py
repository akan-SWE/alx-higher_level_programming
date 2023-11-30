#!/usr/bin/python3
#
def fizzbuzz():
    for number in range(1, 101):
        if not number % 15:  # multiples of 5 and 3
            print('FizzBuzz', end=' ')
        elif not number % 5:  # multiples of 5
            print('Buzz', end=' ')
        elif not number % 3:  # multiples of 3
            print('Fizz', end=' ')
        else:
            print(f'{number}', end=' ')  # not a multiple
