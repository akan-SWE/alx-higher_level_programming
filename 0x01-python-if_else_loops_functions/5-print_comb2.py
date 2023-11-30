#!/usr/bin/python3

for i in range(0, 100):
    print('0' if i < 10 else '', end='')

    print(f'{i}, ' if i < 99 else '{}\n'.format(i), end='')
