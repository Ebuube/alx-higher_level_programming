#!/usr/bin/python3
"""
My GitHub!
- Makes use of Basic Authentication
"""
from requests import get
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    token = argv[2]

    url = "https://api.github.com/user"
    # print("url: {}".format(url))  # for tests
    basic = HTTPBasicAuth(username, token)
    '''
    headers  = {'Authorization': 'Bearer ' + str(token),
                'X-GitHub-Api-Version': '2022-11-28'}
    response = get(url, headers=headers)
    '''
    response = get(url, auth=basic)
    try:
        print(response.json()['id'])
    except Exception:
        print("None")
