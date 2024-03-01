#!/usr/bin/python3
def find_peak(list_of_integers):
    """Find a peak in a list of integers"""
    if list_of_integers:
        peak = list_of_integers[0]
        for num in list_of_integers:
            if num > peak:
                peak = num
        return peak
    else:
        return None
