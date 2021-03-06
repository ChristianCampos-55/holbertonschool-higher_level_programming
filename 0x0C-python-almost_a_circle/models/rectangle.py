#!/usr/bin/python3
""" Module that hosts the Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle which inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rec's constructor with super ID (non-psychology)"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ public method area, returns just that """
        return self.__width * self.__height

    def display(self):
        """ public method display, prints rect with '#' """
        if self.__y:
            for i in range(self.__y):
                print()
        for a in range(self.__height):
            if self.__x:
                for j in range(self.__x):
                    print(' ', end='')
            for b in range(self.__width):
                print('#', end='')
            print()

    def to_dictionary(self):
        """ public method that returns a dict representation of the class """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

    def update(self, *args, **kwargs):
        """ method to update values with args """
        selves = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) != 0:
            for a in range(len(args)):
                setattr(self, selves[a], args[a])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ resignification of __str__ inheritance """
        return ('[Rectangle] (' + str(self.id) + ') ' + str(self.x) + '/' +
                str(self.y) + ' - ' + str(self.width) + '/' + str(self.height))

    @property
    def width(self):
        """ getter width """
        return self.__width

    @width.setter
    def width(self, val):
        """ setter width """
        if type(val) is not int:
            raise TypeError('width must be an integer')
        if val <= 0:
            raise ValueError('width must be > 0')
        self.__width = val

    @property
    def height(self):
        """ getter height """
        return self.__height

    @height.setter
    def height(self, val):
        """ setter height """
        if type(val) is not int:
            raise TypeError('height must be an integer')
        if val <= 0:
            raise ValueError('height must be > 0')
        self.__height = val

    @property
    def x(self):
        """ getter x """
        return self.__x

    @x.setter
    def x(self, val):
        """ setter x """
        if type(val) is not int:
            raise TypeError('x must be an integer')
        if val < 0:
            raise ValueError('x must be >= 0')
        self.__x = val

    @property
    def y(self):
        """ getter y """
        return self.__y

    @y.setter
    def y(self, val):
        """ setter y """
        if type(val) is not int:
            raise TypeError('y must be an integer')
        if val < 0:
            raise ValueError('y must be >= 0')
        self.__y = val
