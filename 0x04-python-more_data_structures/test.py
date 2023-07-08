#!/usr/bin/python3
update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

my_dict = { }
key = "a"
value = "a"
new_dict = update_dictionary(my_dict, key, value)
print_sorted_dictionary(new_dict)
print("xx")
print_sorted_dictionary(my_dict)
