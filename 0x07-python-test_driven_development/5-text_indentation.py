#!/usr/bin/python3
"""Module to print a text with 2 new lines
after each of these characters: ., ? and :"""


def text_indentation(text):
    """
    Method for adding 2 new lines after '.?:' chars

    args:
        text: the str text

    Raises:
        TypeError: If text is not a str
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
