#!/usr/bin/python3
"""
A function that prints the numbers from 1 to 100 separated by a space
For numbers which are multipiles of three print 'Fizz' instead of the number
and for multiples of five print 'Buzz'
"""


def fizzbuzz():
    for count in range(1, 101):
        if (count % 3 == 0) and (count % 5) == 0:
            print('FizzBuzz', end=' ')
        elif count % 3 == 0:
            print('Fizz', end=' ')
        elif count % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(count, end=' ')
# end of function
