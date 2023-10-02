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
    except error.URLError as e:
        if hasattr(e, 'reason'):
            print("We failed to reach a server.")
        elif hasattr(e, 'code'):
            print("The server couldn\'t fulfill the request.")
            print("Error code: {}".format(e.code))
