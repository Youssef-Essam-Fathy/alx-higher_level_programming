#!/usr/bin/python3
"""A module to add integers"""

def add_integer(a, b=98):
    """
    Function to add integers

    args:
        a: first integer
        b: second integer

    Raises:
        TypeError: exception with the message a must be an integer or b must be an integer

    Returns:
        return sum of two integers
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
