#!/usr/bin/python3
"""
A class Square that defines a square by:
Private instance attribute: size
Instantiation with size (int/value verification)
No module importing
"""


class Square:
    """ Defines a square """

    def __init__(self, size=0, position=(0, 0)):
        """
        constructor
        Args:
            size: length of square side
            position: the position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Property to retrieve the length size of the square
        Raises:
            TypeError: If size is not an integer
            ValueError: If size < 0
        """
        return self.__size

    @property
    def position(self):
        """
        Property to retrieve the current position of the square
        Raises:
            TypeError: If size is not an integer
            ValueError: If size < 0
        """
        return self.__position

    @size.setter
    """ To set size value """
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    """ To set position value """
    def position(self, value):
        if not isinstance(value, tuple) or
        len(value) != 2 or
        not all(isinstance(num, int) for num in value) or
        not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        if self.size == 0:
            print()
        for i in range(self.position[1]):
            print("\n")
        for i in range(self.size):
            for j in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()
