#!/usr/bin/python3
""" Files that hosts the load_from_json_file function """
import json


def load_from_json_file(filename):
    """ Creates an object from a Json file """
    with open(filename, encoding="UTF-8") as _file:
        return json.load(_file)
