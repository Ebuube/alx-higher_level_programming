#!/usr/bin/python3
"""
Response header value #1
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    header = 'X-Request-Id'

    response = requests.get(url)
    print(response.headers[header])
