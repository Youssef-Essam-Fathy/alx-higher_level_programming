#!/usr/bin/python3
"""No module importing"""


class MyList(list):
    '''class module that inherits from another class'''

    def print_sorted(self):
        '''Public instance method'''
        sorted_list = sorted(self)
        print(sorted_list)