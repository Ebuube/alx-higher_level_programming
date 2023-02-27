#!/usr/bin/python3
"""Add all of its arguments to a Python list and saves them to a file
"""


from sys import argv
import json

save_to_json_file = __import__(
        '5-save_to_json_file'
        ).save_to_json_file
load_from_json_file = __import__(
        '6-load_from_json_file'
        ).load_from_json_file

filename = "add_item.json"

# Create file if file doesn't exist
try:
    myFile = open(filename, mode="r", encoding="utf-8")
    myFile.close()
except FileNotFoundError:
    with open(filename, mode="w", encoding="utf-8") as myFile:
        json.dump(list(), myFile)

item_list = list(load_from_json_file(filename))

for pos in range(1, len(argv)):
    item_list.append(argv[pos])

save_to_json_file(item_list, filename)
