#!/usr/bin/python3
import sys
my_save = __import__("7-save_to_json_file")
my_load = __import__("8-load_from_json_file")

my_file = []
try:
    my_file = my_load.load_from_json_file("add_item.json")
except:
 """   with open("add_item.json", mode="w") as open_file:
        my_save.save_to_json_file(my_file, "add_item.json")
    my_file = my_load.load_from_json_file("add_item.json")
"""
if len(sys.argv) < 2:
    pass
else:
    for arg in sys.argv[1:]:
        my_file.append(arg)
my_save.save_to_json_file(my_file, "add_item.json")
