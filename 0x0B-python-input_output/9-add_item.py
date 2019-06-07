#!/usr/bin/python3
import os
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
"""
"""


# foo
if os.path.exists("add_item.json"):
    obj = load_from_json_file("add_item.json")
else:
    obj = []
save_to_json_file(obj + argv[1:], "add_item.json")
