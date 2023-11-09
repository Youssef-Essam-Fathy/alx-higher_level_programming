#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    mxval = 0
    mxkey = None
    for key, val in a_dictionary.items():
        if val > mxval:
            mxval = val
            mxkey = key
    return mxkey
