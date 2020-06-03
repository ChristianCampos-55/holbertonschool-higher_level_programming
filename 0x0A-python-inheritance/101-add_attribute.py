#!/usr/bin/python3
""" Module that hosts function that adds an atrribute, if it can """


def add_attribute(instance, name, value):
    if hasattr(instance, '__dict__'):
        setattr(instance, name, value)
    else:
        raise TypeError("can't add new attribute")
