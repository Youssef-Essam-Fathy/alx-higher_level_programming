#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    for i, c in enumerate(str):
        if i != n:
            str2 += c
    return str2
