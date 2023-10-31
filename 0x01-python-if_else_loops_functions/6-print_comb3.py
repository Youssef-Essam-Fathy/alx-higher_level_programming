#!/usr/bin/python3
for num in range(10):
    for k in range(num, 10):
        if num < k:
            print("{:d}{:d}".format(num, k),
                  end="\n" if num == 8 and k == 9 else ", ")
