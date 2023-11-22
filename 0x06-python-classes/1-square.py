#!/usr/bin/python3
"""
A class Square that defines a square by:
Private instance attribute: size
Instantiation with size (no type/value verification)
No module importing
"""
class Square:
    """ Defines a square """
    def __init__(self, size):
        """
        constructor:
        Args:
            size: length of square side
        """
        self.__size = size
