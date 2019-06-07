#!/usr/bin/python3


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ats = {}
        if attrs is None:
            return self.__dict__
        else:
            for key in self.__dict__:
                if key in attrs:
                    ats[key] = self.__dict__[key]
            return ats
