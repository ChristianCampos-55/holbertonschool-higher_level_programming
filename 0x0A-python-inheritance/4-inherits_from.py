#!/usr/bin/python3
""" Module that hosts inherits_from function """


def inherits_from(obj, a_class):
    """ Function that returns whether an obj inherits, strictly,
        from a class """

    return type(obj) is not a_class and isinstance(obj, a_class)
