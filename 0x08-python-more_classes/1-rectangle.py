#!/usr/bin/python3
""" Module that houses rectangle class """


class Rectangle:
    """ Rectangle class, with atributes width and height """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(self.__width) is not int:
            raise TypeError('width must be an integer')
        elif self.__width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(self.__height) is not int:
            raise TypeError('width must be an integer')
        elif self.__height < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__height = height
