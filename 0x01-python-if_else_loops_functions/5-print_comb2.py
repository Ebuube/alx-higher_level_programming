#!/usr/bin/python3
"""To print comma delimited integers from 0 to 99"""

for num in range(0, 100):
    if num < 99:
        print("{}".format(str(num)), end=", ")
    else:
        print("{}".format(str(num)))
