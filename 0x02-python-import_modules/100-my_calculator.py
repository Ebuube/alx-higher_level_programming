#!/usr/bin/python3
"""
A program that imports all functions a file and handles basic operations.
"""


if __name__ == '__main__':
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div


    if (len(argv) != 4):
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    operators = ['+', '-', '*', '/']
    a = int()
    b = int()
    result = 0
    try:    # check if the input operator is valid
        operators.index(argv[2])
    except ValueError:
        print("Unknown operator. Available operators: are +, -, * and /")
        exit(1)

    try:    # reject invalid operands
        a = int(argv[1])
        b = int(argv[3])
    except:
        print("Invalid operands")
        exit(1)

    # get operator
    if (argv[2] == '+'):
        calc = add
    if (argv[2] == '-'):
        calc = sub
    if (argv[3] == '*'):
        calc = mul
    if (argv[2] == '/'):
        calc = div

    result = calc(a, b)
    print("{:d} {:s} {:d} = {}".format(a, argv[2], b, result))
