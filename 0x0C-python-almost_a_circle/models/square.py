#!/usr/bin/python3
"""A Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """init the Square
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """overwrite the str method
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size of square getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """size of square setter
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the square
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs["id"]
                if key == "size":
                    self.size = kwargs["size"]
                if key == "x":
                    self.x = kwargs["x"]
                if key == "y":
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """stores square as dict
        """
        my_dict = {}
        my_dict["id"] = self.id
        my_dict["size"] = self.size
        my_dict["x"] = self.x
        my_dict["y"] = self.y
        return my_dict
