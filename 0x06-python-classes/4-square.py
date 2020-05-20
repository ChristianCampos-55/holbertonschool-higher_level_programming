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

    """ method to get are of Square """
    def area(self):
        return self.__size ** 2

    """ set getter """
    @property
    def size(self):
        return self.__size

    """ set setter (yeah, I know) """
    @size.setter
    def __init__(self, value):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
