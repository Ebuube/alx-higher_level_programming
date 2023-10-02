#!/usr/bin/python3
"""
What is my status? #1
"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)
    msg = response.text
    print("Body response:")
    print("\t- type: {}".format(type(msg)))
    print("\t- content: {}".format(msg))
