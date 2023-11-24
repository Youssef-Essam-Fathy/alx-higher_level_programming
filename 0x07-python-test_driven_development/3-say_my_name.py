#!/usr/bin/python3
"""Module to print first and last names"""


def say_my_name(first_name, last_name=""):
    """
    Method for displaying first and last names

    args:
        first_name: first name string
        last_name: last name string

    Raises:
        TypeError: if first_name and last_name aren't string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
