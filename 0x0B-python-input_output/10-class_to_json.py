#!/usr/bin/python3
""" File that hosts the class_to_json function """


def class_to_json(obj):
    """ function that returns the dict description for JSON
        serialization of an object """

    return obj.__dict__
