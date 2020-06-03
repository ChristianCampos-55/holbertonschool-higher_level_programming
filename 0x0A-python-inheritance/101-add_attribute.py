#!/usr/bin/python3
""" Module that hosts function that adds an atrribute, if it can """


def add_attribute(obj, name, val):
    if not hasattr(obj, '__dic__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, val)
