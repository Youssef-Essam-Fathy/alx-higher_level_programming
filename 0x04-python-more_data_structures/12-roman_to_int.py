#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    ttl = 0
    nm = 0
    di = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in reversed(roman_string):
        nm = di[i]
        ttl += nm if ttl < nm * 5 else -nm
    return ttl
