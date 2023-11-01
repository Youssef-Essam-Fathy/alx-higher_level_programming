#!/usr/bin/python3
def uppercase(str):
    for cr in str:
        if ord(cr) in range(97, 123):
            cr = chr(ord(cr) - 32)
        else:
            cr = chr(ord(cr))
        print("{}".format(cr), end="")
    print("")
