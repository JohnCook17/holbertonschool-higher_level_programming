#!/usr/bin/python3
"""A Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """A Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """init class
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter
        """
        return self.__width

    @property
    def height(self):
        """height getter
        """
        return self.__height

    @property
    def x(self):
        """x getter
        """
        return self.__x

    @property
    def y(self):
        """y getter
        """
        return self.__y

    @width.setter
    def width(self, value):
        """width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """x setter
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates the area
        """
        return self.width * self.height

    def display(self):
        """prints to stdout
        """
        i = 0
        print("\n" * self.y, end="")
        while i < self.height:
            print(" " * self.x, end="")
            print("#" * self.width)
            i += 1

    def __str__(self):
        """overwrites the str method and provides the wanted output
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """updates the Rectangle
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs["id"]
                if key == "width":
                    self.width = kwargs["width"]
                if key == "height":
                    self.height = kwargs["height"]
                if key == "x":
                    self.x = kwargs["x"]
                if key == "y":
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """writes the instance to a dict
        """
        my_dict = {}
        my_dict["id"] = self.id
        my_dict["width"] = self.width
        my_dict["height"] = self.height
        my_dict["x"] = self.x
        my_dict["y"] = self.y
        return my_dict
