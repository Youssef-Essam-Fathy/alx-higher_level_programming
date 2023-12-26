#!/usr/bin/python3
"""No module importing"""


class BaseGeometry():
    '''class'''
    def area(self):
        '''Constructor1'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Constructor2'''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
