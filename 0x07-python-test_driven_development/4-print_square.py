#!/usr/bin/python3
""" Module that hosts function print_square """


def print_square(size):
    """ function that prints a square with '#' based
        on the 'size' received """

    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
