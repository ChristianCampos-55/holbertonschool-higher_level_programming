#!/usr/bin/python3
""" Module that hosts the Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle which inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rec's constructor with super ID (non-psychology)"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter width """
        return self.__width

    @width.setter
    def width(self, width):
        """ setter width """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """ getter height """
        return self.__height

    @height.setter
    def height(self, height):
        """ setter height """
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """ getter x """
        return self.__x

    @x.setter
    def x(self, x):
        """ setter x """
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """ getter y """
        return self.__y

    @y.setter
    def y(self, y):
        """ setter y """
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if x < 0:
            raise ValueError('y must be >= 0')
        self.__y = y
