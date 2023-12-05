#!/usr/bin/python3
"""No module importing"""


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file”"""
    import json
    with open(filename, 'r') as file:
      return json.load(file)
