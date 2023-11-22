#!/usr/bin/python3
"""
A class Square that defines a square by:
Private instance attribute: size
Instantiation with size (int/value verification)
No module importing
"""


class Square:
    """ Defines a square """

    def __init__(self, size=0):
        """
        constructor
        Args:
            size: length of square side
        Raises:
            TypeError: If size is not an integer
            ValueError: If size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
