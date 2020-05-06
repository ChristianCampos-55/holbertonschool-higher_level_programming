#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        space = ""
        for i in x:
            print("{:s}{:d}".format(space, i), end="")
            space = " "
        print()
