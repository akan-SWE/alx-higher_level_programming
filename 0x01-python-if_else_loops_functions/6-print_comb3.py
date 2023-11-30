#!/usr/bin/python3

for i in range(0, 10):
    for j in range(i + 1, 10):
        print('{}'.format(i), end='')  # first digit
        print('{}\n'.format(j) if i == 8 and j == 9
              else '{}, '.format(j), end='')  # second digit
