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


    @width.setter
    """ setter width """
    def width(self, width):
        self.__width = width

    @property
    """ getter width """
    def width(self):
        return self.__width

    @height.setter
    """ setter height """
    def height(self, height):
        self.__height = height

    @property
    """ getter height """
    def height(self):
        return self.__height

    @x.setter
    """ setter x """
    def x(self, x):
        self.__x = x

    @property
    """ getter x """
    def x(self):
        return self.__x

   @y.setter
    """ setter y """
    def y(self, y):
        self.__y = y

    @property
    """ getter y """
    def y(self):
        return self.__y
