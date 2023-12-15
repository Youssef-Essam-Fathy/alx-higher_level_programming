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
