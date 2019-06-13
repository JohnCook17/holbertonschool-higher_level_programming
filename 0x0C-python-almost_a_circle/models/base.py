#!/usr/bin/python3
"""A base class for the rest of the project

"""
import json
import csv


class Base:
    """A base class for the rest of the project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Inits the var id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Takes a list of dicts and changes it to a json string
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves as class_name.json, the contents of list_objs
        """
        file_name = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
            with open(file_name, mode="w+", encoding="utf-8") as my_file:
                my_file.write(list_objs)
        else:
            my_list = []
            for obj in list_objs:
                my_dict = {}
                for _ in obj.to_dictionary():
                    my_dict = obj.to_dictionary()
                my_list.append(my_dict)
            data = Base.to_json_string(my_list)
            with open(file_name, mode="w+", encoding="utf-8") as my_file:
                my_file.write(data)

    @staticmethod
    def from_json_string(json_string):
        """Takes a json string and loads it
        """
        if json_string is None or not json_string:
            json_string = {}
            return json_string
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a new instance of a class
        """
        if cls.__name__ == "Rectangle":
            from models.rectangle import Rectangle
            dummy = Rectangle(width=1, height=1, x=0, y=0, id=None)
            dummy.update(**dictionary)
            return dummy
        elif cls.__name__ == "Square":
            from models.square import Square
            dummy = Square(size=1, x=0, y=0, id=None)
            dummy.update(**dictionary)
            return dummy
        else:
            pass

    @classmethod
    def load_from_file(cls):
        """Loads a class from a file
        """
        if cls.__name__ == "Rectangle":
            import os
            from models.rectangle import Rectangle
            if os.path.exists("Rectangle.json"):
                with open("Rectangle.json", mode="r") \
                        as my_file:
                    file_data = cls.from_json_string(my_file.read())
                    r = []
                    for my_dict in file_data:
                        rect = Rectangle.create(**my_dict)
                        r.append(rect)
                    return r
            else:
                my_file = {}
                return my_file
        elif cls.__name__ == "Square":
            import os
            from models.square import Square
            if os.path.exists("Square.json"):
                with open("Square.json", mode="r")\
                        as my_file:
                    file_data = cls.from_json_string(my_file.read())
                    r = []
                    for my_dict in file_data:
                        rect = Square.create(**my_dict)
                        r.append(rect)
                    return r
            else:
                my_file = {}
                return my_file

    @classmethod
    def save_to_file_csv(cls, list_objs):
        if list_objs is None:
            list_objs = []
        if cls.__name__ == "Rectangle":
            from models.rectangle import Rectangle
            fields = ["id", "width", "height", "x", "y"]
            file_name = cls.__name__ + ".csv"
            with open(file_name, mode="w") as csv_file:
                write_head = 0
                for obj in list_objs:
                    my_csv = obj.to_dictionary()
                    dict_writer = csv.DictWriter(csv_file, fieldnames=fields)
                    if write_head == 0:
                        dict_writer.writeheader()
                        write_head = 1
                    dict_writer.writerow(my_csv)
        elif cls.__name__ == "Square":
            from models.square import Square
            fields = ["id", "size", "x", "y"]
            file_name = cls.__name__ + ".csv"
            with open(file_name, mode="w") as csv_file:
                write_head = 0
                for obj in list_objs:
                    my_csv = obj.to_dictionary()
                    dict_writer = csv.DictWriter(csv_file, fieldnames=fields)
                    if write_head == 0:
                        dict_writer.writeheader()
                        write_head = 1
                    dict_writer.writerow(my_csv)
        else:
            pass

    @classmethod
    def load_from_file_csv(cls):
        if cls.__name__ == "Rectangle":
            import os
            from models.rectangle import Rectangle
            if os.path.exists("Rectangle.csv"):
                with open("Rectangle.csv", mode="r") as csv_file:
                    retval = []
                    csv_reader = csv.DictReader(csv_file)
                    for dct in map(dict, csv_reader):
                        for key in dct:
                            dct[key] = int(dct[key])
                        rect = Rectangle.create(**dct)
                        retval.append(rect)
                    return retval
            else:
                my_file = {}
                return my_file
        elif cls.__name__ == "Square":
            import os
            from models.square import Square
            if os.path.exists("Square.csv"):
                with open("Square.csv", mode="r") as csv_file:
                    retval = []
                    csv_reader = csv.DictReader(csv_file)
                    for dct in map(dict, csv_reader):
                        for key in dct:
                            dct[key] = int(dct[key])
                        sqr = Square.create(**dct)
                        retval.append(sqr)
                    return retval
            else:
                my_file = {}
                return my_file
