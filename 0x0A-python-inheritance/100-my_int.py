#!/usr/bin/python3
""" Method that hosts MyInt class, which inherits from int and swaps
    == and != operators """


class MyInt(int):
    """ swapping operators functionality """

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__qe__(other)
