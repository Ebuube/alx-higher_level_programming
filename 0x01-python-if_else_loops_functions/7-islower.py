#!/usr/bin/python3
"""A function that checks for lowercase character."""

def islower(c):
    try:
        c = int(c)
    except:
        sys.exit(1)

    if c >= 97 and c <= 122:
        value = True
    else:
        value = False
    return (value)
#end of function

print("The letter \'a\' is lower? (True/False): ", islower('a'))
