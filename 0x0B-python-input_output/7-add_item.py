#!/usr/bin/python3
"""No module importing"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

listarg = list(sys.argv[1:])

try:
    present_data = load_from_json_file('add_item.json')
except Exception:
    present_data = []

present_data.extend(listarg)

save_to_json_file(present_data, 'add_item.json')
