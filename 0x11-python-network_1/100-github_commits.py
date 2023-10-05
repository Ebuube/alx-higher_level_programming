#!/usr/bin/python3
"""
Search API
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    try:
        repo_name = str(argv[1])
        user = str(argv[2])
    except IndexError:
        print("Usage: {} user repository".format(argv[0]))
        exit()

    url = 'https://api.github.com/repos/{}/{}/commits'.format(
                user, repo_name)
    # Sample
    # https://api.github.com/repos/Ebuube/AirBnB_clone/commits/master

    response = get(url)

    try:
        js_res = response.json()
    except ValueError:
        exit()

    if len(js_res) == 0 or js_res is None:
        pass
    else:
        count = 0
        max_len = 10
        for i in js_res:
            if count >= max_len:
                break
            sha = i['sha']
            author_name = i['commit']['author']['name']
            print("{}: {}".format(sha, author_name))
            count += 1
