#!/usr/bin/python3
"""No module importing"""


def read_file(filename=""):
    """
    a function that reads a text file (UTF8)
    and prints it to stdout
    args:
        filename: the  name of the file to read
    """
    with open(filename, 'r', encoding="utf-8") as file:
        file_read = file.read()
        print(file_read)
