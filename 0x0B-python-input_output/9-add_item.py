#!/usr/bin/python3
""" Script that adds arguments to a python list """
from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = 'add_item.json'

try:
    _list = load_from_json_file(filename)
except Exception:
    _list = []

for i in argv[1:]:
    _list.append(i)

save_to_json_file(_list, filename)
