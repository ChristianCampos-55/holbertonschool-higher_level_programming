#!/usr/bin/python3
""" File that hosts the save_to_json_file function """
import json


def save_to_json_file(my_obj, filename):
    """ Function that writes and object to a text file using
        json representation """
    with open(filename, mode='w') as _file:
        _file.write(json.dumps(my_obj))
