#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for submatt in matrix:
        if len(submatt) == 0:
            print()
        for idx in range(len(submatt)):
            print("{:d}".format(submatt[idx]),
                  end="\n" if idx is len(submatt) - 1 else " ")
