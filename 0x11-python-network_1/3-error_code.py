#!/usr/bin/python3
"""
Error code #0
"""
from urllib import (request, error)
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    try:
        with request.urlopen(url) as response:
            response
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
