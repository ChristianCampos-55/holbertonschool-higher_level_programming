#!/usr/bin/python3
""" File that hosts the read_file function """


def read_file(filename=""):
    """ returns each line in opened file """
    with open(filename, encoding='UTF-8') as fi:
        for i in fi:
            print(i, end='')
