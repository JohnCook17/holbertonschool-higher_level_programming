#!/usr/bin/python3
def inherits_from(obj, a_class):
    if not isinstance(obj, a_class) or not type(obj) is a_class:
        return True
    else:
        return False
