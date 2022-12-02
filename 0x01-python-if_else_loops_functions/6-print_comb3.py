#!/usr/bin/python3
"""prints all the different combinations of two digits"""
for first_digit in range(0, 9):
    for second_digit in range(1, 10):
        if (first_digit == 8) and (second_digit == 9):
            print("{}{}".format(first_digit, second_digit), end="\n")
        else:
            print("{}{}".format(first_digit, second_digit), end=", ")
