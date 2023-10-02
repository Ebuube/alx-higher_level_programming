#!/usr/bin/python3
"""
0. What's my status? #0
"""
from urllib import request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        msg = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(msg)))
        print("\t- content: {}".format(msg))
        print("\t- utf8 content: {}".format(msg.decode('utf-8')))
