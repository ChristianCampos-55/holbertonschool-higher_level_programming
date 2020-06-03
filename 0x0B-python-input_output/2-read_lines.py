#!/usr/bin/python3
""" File that hosts the read_lines function """


def read_lines(filename="", nb_lines=0):
    """ Function that reads a specific number (nb_lines)
        of lines in a document """

    with open(filename, encoding='UTF-8') as fi:
        if nb_lines:
            for countr in range(nb_lines):
                print(fi.readline(), end='')
        else:
            for line in fi:
                print(line, end='')
