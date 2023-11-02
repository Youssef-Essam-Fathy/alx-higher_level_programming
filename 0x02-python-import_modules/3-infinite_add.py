#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    addi = 0
    arg0 = len(sys.argv) - 1
    for i in range(arg0):
        addi += int(sys.argv[i + 1])
    print(addi)
