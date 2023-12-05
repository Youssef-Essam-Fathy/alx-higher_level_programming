#!/usr/bin/python3
"""No module importing"""


def save_to_json_file(my_obj, filename):
    """ a function that writes an Object to a text file,
        using a JSON representation"""
    import json
    with open(filename, "w") as file:
        return json.dump(my_obj, file)
