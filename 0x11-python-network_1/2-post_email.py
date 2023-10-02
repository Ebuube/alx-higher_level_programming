#!/usr/bin/python3
"""
POST an email #0
"""
from urllib import (parse, request)
import sys


if __name__ == '__main__':
    values = {'email': sys.argv[2]}
    url = sys.argv[1]

    data = parse.urlencode(values)
    data = data.encode('ascii')     # data should be bytes
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        msg = response.read()
        print(msg.decode('utf-8'))
