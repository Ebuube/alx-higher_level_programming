#!/usr/bin/python3
"""
POST an email #1
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)
