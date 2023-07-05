#!/usr/bin/python3
"""
A program that imports all functions a file and handles basic operations.
"""


if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

    if (len(sys.argv) != 4):
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
        operators = {"+": add, "-": sub, "*": div, "/": div}

        if operator in operators.keys():
            calc = operators[operator]
            print("{} {} {} = {}".format(a, operator, b, calc(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
