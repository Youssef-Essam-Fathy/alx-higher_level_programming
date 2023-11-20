#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    indx, j = 0, 0
    while indx < x:
        try:
            print("{:d}".format(my_list[indx]), end="")
            j += 1
        except (TypeError, ValueError):
            pass
        indx += 1
    print()
    return j
