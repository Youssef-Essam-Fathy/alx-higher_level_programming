#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    idx = 0
    try:
        while idx is not x:
            print(mylist[i], end='')
            idx += 1
    except IndexError:
        None
    print()
    return idx
