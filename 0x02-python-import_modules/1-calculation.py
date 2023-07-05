#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import (sub, add, mul, div)
    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {:g}".format(a, b, div(a, b)))
