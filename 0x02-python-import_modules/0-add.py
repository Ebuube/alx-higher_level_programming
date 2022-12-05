#!/usr/bin/python3
"""
A program to import and use a function
"""



if __name__ == '__main__':
    from add_0 import add
    a = 1
    b = 2
    print('{} + {} = {}'.format(
        str(a), str(b), str(add(a, b))))
