#!/usr/bin/python3
""" File that hosts the append_write function """


def append_write(filename="", text=""):
    """ Function tha appends a set of characters (text) to a file
        and returns the number of hcaracters added """

    with open(filename, mode='a', encoding='UTF-8') as _file:
        return _file.write(text)
