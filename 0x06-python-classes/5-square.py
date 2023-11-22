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

    @property
    def size(self):
        """
        Property to retrieve the length size of the square
        Raises:
            TypeError: If size is not an integer
            ValueError: If size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Public instance method
        Returns:
            The size of square squared
        """

        return self.__size ** 2

    def my_print(self):
        """ Public instance method
        Prints:
            The square with the character # in stdout
        """
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and j != i else "")
        print()
