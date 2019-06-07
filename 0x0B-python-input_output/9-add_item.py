#!/usr/bin/python3
import sys
my_save = __import__("7-save_to_json_file")
my_load = __import__("8-load_from_json_file")


try:
    obj = my_load.load_from_json_file("add_item.json")
except:
    obj = []
if not len(sys.argv) < 2:
    my_save.save_to_json_file(obj + sys.argv[1:], "add_item.json")
