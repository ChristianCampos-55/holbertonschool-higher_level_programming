#!/usr/bin/python3
""" Class Square """

class Square:

    """ definition of size method, with excepted edge cases """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    """ set size getter """
    @property
    def size(self):
        return self.__size

    """ set size setter (yeah, try saying that three times) """
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    """ method to get area of Square """
    def area(self):
        return self.__size ** 2
