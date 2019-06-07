#!/usr/bin/python3
import sys
my_save = __import__("7-save_to_json_file")
my_load = __import__("8-load_from_json_file")

obj = []
try:
    obj = my_load.load_from_json_file("add_item.json")
except:
 """   with open("add_item.json", mode="w") as open_file:
        my_save.save_to_json_file(my_file, "add_item.json")
    my_file = my_load.load_from_json_file("add_item.json")
"""
if not len(sys.argv) < 2:
    for arg in sys.argv[1:]:
        obj.append(arg)
my_save.save_to_json_file(obj, "add_item.json")
