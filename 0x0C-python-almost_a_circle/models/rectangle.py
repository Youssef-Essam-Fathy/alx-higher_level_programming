#!/usr/bin/python3
'''importing Base class module'''

from models.base import Base


class Rectangle(Base):
    '''A class representation area'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__height <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        if not isinstance(self.__x, int):
            raise TypeError("x must be an integer")
        if self.__x < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
        if not isinstance(self.__y, int):
            raise TypeError("y must be an integer")
        if self.__y < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        '''Calcaulate and return the area of the rectangle'''
        return self.width * self.height

    def display(self):
        '''prints in stdout the Rectangle instance with the character #'''
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        '''Return a string representation of the Rectangle instance'''
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )

    def update(self, *args):
        '''assigns an argument to each attribute'''
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
