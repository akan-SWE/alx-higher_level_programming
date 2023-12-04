#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    import calculator_1

    def calculator():
        """ A calculator that handles basic operations
        Return:
         void (nothing)
        """
        argc = len(sys.argv)  # number of arguments
        expected_arguments = 4  # including program name

        if argc != expected_arguments:
            print('Usage: ./100-my_calculator.py <a> <operator> <b>')
            sys.exit(1)

        num1 = int(sys.argv[1])  # first integer
        operator = sys.argv[2]  # the operator
        num2 = int(sys.argv[3])  # second integer

        result = 0
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)

        print('{} {} {} = {}'.format(num1, operator, num2, result))

    calculator()
