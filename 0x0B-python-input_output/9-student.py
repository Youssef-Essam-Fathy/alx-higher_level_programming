#!/usr/bin/python3
"""No module importing"""


class Student:
    """representation of a class"""
    def __init__(self, first_name, last_name, age):
        """Instantiation of a class"""
        self.fr_name = first_name
        self.ls_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance"""
        return self.__dict__
