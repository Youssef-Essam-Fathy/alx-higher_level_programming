#!/usr/bin/python3
"""No module importing"""


def is_kind_of_class(obj, a_class):
    return type(obj) is a_class or type(obj) is super(a_class)
