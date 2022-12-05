#!/usr/bin/python3
"""
A program that imports functions from the file calculator_1.py
and does some maths and prints the result.
"""


if __name__ == '__main__':
    from calculator_1 import sub
    from calculator_1 import add
    from calculator_1 import mul
    from calculator_1 import div

    a = 10
    b = 5

    my_str = "{} + {} =".format(a, b)
    print(my_str, add(a, b))
    my_str = "{} - {} =".format(a, b)
    print(my_str, sub(a, b)
    my_str = "{} * {} =".format(a, b)
    print(my_str, mul(a, b))
    my_str = "{} / {} =".format(a, b)
    print(my_str, div(a, b))
