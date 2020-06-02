#!/usr/bin/python3
""" Module that hosts MyList class """


class MyList(list):
    """ Method to a sorted list """

    def print_sorted(self):
        print(sorted(self))
