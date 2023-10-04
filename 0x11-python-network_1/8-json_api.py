#!/usr/bin/python3
"""
Search API
"""
from requests import post
from sys import argv


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    try:
        query = argv[1]
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
