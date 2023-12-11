#!/usr/bin/python3
''' No module importing '''


class Base:
    ''' a representation for our oop '''
    
    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects