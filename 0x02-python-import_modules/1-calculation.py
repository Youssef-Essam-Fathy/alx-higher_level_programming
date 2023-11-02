#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    sum, minus, multip, quot = add(a, b), sub(a, b), mul(a, b), div(a, b)
    print("{} + {} = {}".format(a, b, sum))
    print("{} - {} = {}".format(a, b, minus))
    print("{} * {} = {}".format(a, b, multip))
    print("{} / {} = {}".format(a, b, quot))
