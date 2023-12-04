#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    # Get number of arguments and output
    argc = len(sys.argv)
    if argc == 1:
        print('{} arguments.'.format(argc - 1))
    elif argc == 2:
        print('{} argument:'.format(argc - 1))
    elif argc > 2:
        print('{} arguments:'.format(argc - 1))
    # output arguments
    i = 1
    for arguments in sys.argv[1:]:
        print('{}: {}'.format(i, arguments))
        i += 1
