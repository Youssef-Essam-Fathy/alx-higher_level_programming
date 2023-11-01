#!/usr/bin/python3
for num in range(25, -1, -1):
    c = num + ord('A')
    if num & 1 == 1:
        c += 32
    print("{:c}".format(c), end="")
