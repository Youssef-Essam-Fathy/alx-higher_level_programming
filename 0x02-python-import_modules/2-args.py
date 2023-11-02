#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg0 = len(sys.argv) - 1
    if arg0 == 0:
        print("0 arguments.")
    elif arg0 == 1:
        print("1 argument:")
    else:
        print(f"{arg0} arguments:")
    for args in range(arg0):
        print(f"{args + 1}: {sys.argv[args + 1]}")
