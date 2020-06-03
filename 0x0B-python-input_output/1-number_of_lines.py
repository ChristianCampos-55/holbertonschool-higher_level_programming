#!/usr/bin/python3
""" File that hosts number_of_lines function """


def number_of_lines(filename=""):
    """ A function that returns the number of lines in a file """
    num_of_lines = 0
    with open(filename, encoding='UTF-8') as fi:
        for i in fi:
            num_of_lines += 1
        return num_of_lines
