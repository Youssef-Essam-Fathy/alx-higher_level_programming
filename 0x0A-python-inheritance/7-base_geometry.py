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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
