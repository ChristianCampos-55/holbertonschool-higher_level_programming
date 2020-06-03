#!/usr/bin/python3
""" File that hosts the write_file function """


def write_file(filename="", text=""):
    """ function that writes a set of characters (text) and
        returns the number of characters written """

    with open(filename, mode='w', encoding='UTF-8') as _file:
        return _file.write(text)
