#!/usr/bin/python3
"""
A program that prints the result of the additionof all arguments
"""


if __name__ == '__main__':
    from sys import argv
    sum_args = int()
    for num in range(len(argv) - 1):
        sum_args += int(argv[num + 1])
    print(sum_args)
