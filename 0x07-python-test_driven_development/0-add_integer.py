#!/usr/bin/python3
""" Module that hosts add_integer function. """


def add_integer(a, b=98):
    """
    The function returns the sum of two numbers (a, b)
    which are supossed to be either integers or floats,
    (both are casted into integers in case they are floats).
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
