#!/usr/bin/python3
""" File that hosts the from_json_string function """
import json


def from_json_string(my_str):
    """ Function that returns a json object """
    return json.loads(my_str)
