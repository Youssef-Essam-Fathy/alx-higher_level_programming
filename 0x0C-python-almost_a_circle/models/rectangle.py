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
            raise TypeError(f"{self.__width} must be an integer")
        if self.__width <= 0:
            raise ValueError(f"{self.__width} must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(self.__height, int):
            raise TypeError(f"{self.__height} must be an integer")
        if self.__height <= 0:
            raise ValueError(f"{self.__height} must be > 0")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        if not isinstance(self.__x, int):
            raise TypeError(f"{self.__x} must be an integer")
        if self.__x < 0:
            raise ValueError(f"{self.__x} must be >= 0")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
        if not isinstance(self.__y, int):
            raise TypeError(f"{self.__y} must be an integer")
        if self.__y < 0:
            raise ValueError(f"{self.__y} must be >= 0")
