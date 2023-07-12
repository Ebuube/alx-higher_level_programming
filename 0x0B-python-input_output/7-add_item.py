#!/usr/bin/python3
"""
This module adds all arguments to a Python list, and then save them to a file
"""
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "./add_item.json"      # file to save objects
enc = "utf-8"       # Encoding to use
my_list = list()

if len(sys.argv) > 1 and os.path.exists(filename):
    # Feed arguments to list
    my_list = load_from_json_file(filename)
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])

# Save object
save_to_json_file(my_list, filename)
