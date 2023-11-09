#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for k, v in sorted(a_dictionary.items()):
        if v % 2 == 0:
            print("{}: {:d}".format(k, v))
