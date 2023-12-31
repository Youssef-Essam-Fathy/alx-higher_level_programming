#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    n1 = int(sys.argv[1])
    n3 = int(sys.argv[3])
    oper = sys.argv[2]
    if oper == "+":
        print("{} + {} = {}".format(n1, n3, add(n1, n3)))
    elif oper == "-":
        print("{} - {} = {}".format(n1, n3, sub(n1, n3)))
    elif oper == "*":
        print("{} * {} = {}".format(n1, n3, mul(n1, n3)))
    elif oper == "/":
        print("{} / {} = {}".format(n1, n3, div(n1, n3)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
