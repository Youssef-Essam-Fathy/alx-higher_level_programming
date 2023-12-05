#!/usr/bin/python3
"""No module importing"""


def append_write(filename="", text=""):
    """
    a function that  appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    args:
        filename: the  name of the file to write to
        text: the text to be written in the file
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
