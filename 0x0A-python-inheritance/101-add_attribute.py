#!/usr/bin/python3
""" Method that hosts a function that adds an atribute, if it can """


def add_attribute(obj, name, value):
    if hasattr(obj, '__dic__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
