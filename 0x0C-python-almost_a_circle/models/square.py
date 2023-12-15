#!/usr/bin/python3
'''importing Rectangle class module'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''A class representation area'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor'''
        super().__init__(id, x, y, size, size)

    @property
    def size(self):
        '''Getter for the size'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter for the size'''
        self.width = value
        self.height = value

    def __str__(self):
        '''Return a string representation of the square instance'''
        return (
            f"[Square] ({self.id}) {self.x}/{self.y} - "
            f"{self.size}"
        )

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.x = args[1]
            if len(args) >= 3:
                self.y = args[2]
            if len(args) >= 4:
                self.size = args[3]

        for key, value in kwargs.items():
            setatrr(self, key, value)
