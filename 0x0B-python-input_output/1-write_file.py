#!/usr/bin/python3
"""No module importing"""


def write_file(filename="", text=""):
    """
    a function that writes a text file (UTF8)
    and returns the number of characters written
    args:
        filename: the  name of the file to write to
        text: the text to be written in the file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text, end="")
    return file.tell()
