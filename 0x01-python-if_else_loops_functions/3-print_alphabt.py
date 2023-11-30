#!/usr/bin/python3

for i in range(0, 26):
    print('', end=('' if chr(97 + i) == 'q' or chr(97 + i) == 'e'
                   else '{}'.format(chr(97 + i))))
