#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs == None:
            return self.__dict__
        else:
            for key in self.__dict__:
                if key in attrs:
                    return (key, self.__dict__[key])
    def reload_from_json(self, json):
        return self.__dict__
