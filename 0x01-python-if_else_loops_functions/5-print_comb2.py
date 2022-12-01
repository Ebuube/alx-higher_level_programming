#!/usr/bin/python3
"""To print comma delimited integers from 0 to 99"""

for num in range(0, 100):
    if num < 99:
        print("{:02}".format(num), end=", ")
    else:
        print("{}".format(num))
