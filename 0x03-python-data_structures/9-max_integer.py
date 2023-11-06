#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    cop_l = my_list.copy()
    cop_l.sort()
    cop_l.reverse()
    return cop_l[0]
