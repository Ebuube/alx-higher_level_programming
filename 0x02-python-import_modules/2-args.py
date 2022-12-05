#!/usr/bin/python3
"""
A program that prints the number of and the list of its arguments.
"""


if __name__ == "__main__":
    from sys import argv
    if (len(argv)) == 1:
        print("{} arguments".format(len(argv) - 1), end='')
    elif (len(argv)) == 2:
        print("{} argument".format(len(argv) - 1), end='')
    else:
        print("{} arguments".format(len(argv) - 1), end='')
    if (len(argv)) == 1:
        print('.')
    else:
        print(':')
    if (len(argv)) > 1:
        for count in range(1, len(argv)):
            print("{}: {}".format(str(count), argv[count]))
