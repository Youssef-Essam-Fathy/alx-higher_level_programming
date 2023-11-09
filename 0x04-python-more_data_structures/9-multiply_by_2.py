#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for k, v in a_dictionary.items():
        v2 = v * 2
        print("{}: {:d}".format(k, v2))
