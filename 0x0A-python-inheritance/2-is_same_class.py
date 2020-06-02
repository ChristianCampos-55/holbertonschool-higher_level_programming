#!/usr/bin/python3
""" Module that hosts the is_same_class function """


def is_same_class(obj, a_class):
    """ Function that returns, booleanly, whether an obj
        is exactly an instance of a class """

    return type(obj) == a_class
