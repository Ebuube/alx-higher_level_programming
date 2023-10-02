#!/usr/bin/python3
"""
Response header value #0
"""
from urllib import request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    header = 'X-Request-Id'
    with request.urlopen(url) as response:
        print("{}".format(response.getheader(header)))
