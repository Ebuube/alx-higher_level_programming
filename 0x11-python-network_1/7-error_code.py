#!/usr/bin/python3
"""
Error code #1
"""
from requests import post
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    response = post(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
