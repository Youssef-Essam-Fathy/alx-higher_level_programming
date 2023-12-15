#!/usr/bin/python3
'''importing json module'''
import json


class Base:
    '''a representation for our oop'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        file_name = cls.__name__ + ".json"
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs]
            )
        with open(file_name, 'w') as file:
            file.write(json_string)
