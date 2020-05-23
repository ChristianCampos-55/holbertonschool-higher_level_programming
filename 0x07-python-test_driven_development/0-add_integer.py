#!/usr/bin/python3
""" A function that adds 2 numbers """


def add_integer(a, b=98):
    """
    The function returns the sum of both numbers,
    which are supossed to be either integers or floats,
    (or casted).
    """

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    if type(a) is not int:
        raise TypeError('a must be an integer')
    if type(b) is not int:
        raise TypeError('b must be an integer')

    return a + b
