#!/usr/bin/python3
"""No module importing"""


def from_json_string(my_str):
    """a function that returns an object (Python data structure)
       represented by a JSON string"""
    import json
    return json.loads(my_str)
