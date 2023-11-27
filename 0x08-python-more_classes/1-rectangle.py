#!/usr/bin/python3
"""No module importing"""


class Rectangle:
    """Define a rectangle"""
    def __init__(self, width=0, height=0):
        """
        Constructor
        Args:
            width: the ractangle width
            height: the rectangle height
        """
        self.width = width
        self.height = height

    @property
    """
    property to retreive the width
    """
    def width(self):
        return self.__width

    @width.setter
    """
    Raises:
        TypeError: if width isn't an integer
        ValueError: if width < 0
    """
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    """
    property to retreive the height
    """
    def height(self):
        return self.__width

    @height.setter
    """
    Raises:
        TypeError: if height isn't an integer
        ValueError: if height < 0
    """
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
