#!/usr/bin/python3
"""No module importing"""


class Rectangle:
    """Define a rectangle"""

    def __init__(self, width=0, height=0):
        """Intialize the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """returns the printable representations for the rectangle"""
        strg = ""
        if self.__width != 0 and self.__height != 0:
            strg += "\n".join("#" * self.__width
                              for u in range(self.__height))
        return strg
