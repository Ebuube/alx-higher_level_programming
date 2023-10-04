#!/usr/bin/python3
"""
Search API
"""
from requests import post
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        query = argv[2]
    except IndexError:
        query = ""

    payload = {'q': query}
    response = post(url, data=payload)
    js_res = response.json()
    if type(js_res) is not dict:
        print("Not a valid JSON")
    elif len(js_res) == 0:
        print("No result")
    else:
        print("[{}] {}".format(js_res['id'], js_res['name']))
