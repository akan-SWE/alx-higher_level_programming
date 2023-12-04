#!/usr/bin/python3

# execute only as script and not as an imported module
if __name__ == '__main__':

    def sum_all():
        """Adds all arguments and outputs the result

        Returns:
            The addition of all the arguments
        """
        import sys

        number = 0
        for arguments in sys.argv[1:]:
            number += int(arguments)

        return number

    print('{}'.format(sum_all()))
