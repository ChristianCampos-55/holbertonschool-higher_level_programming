#!/usr/bin/python3
""" Module that hosts class Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Module that validates width and height values by inheriting
        from BaseGeometry class. It also prints and states the area
        of the rectangle"""

    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return'[Rectangle] {}/{}'.format(self.__width, self.__height)
