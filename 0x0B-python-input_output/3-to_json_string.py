#!/usr/bin/python3
"""No module importing"""


def to_json_string(my_obj):
    """a function that returns the JSON
    representation of an object (string)"""
    import json
    return json.dumps(my_obj)
