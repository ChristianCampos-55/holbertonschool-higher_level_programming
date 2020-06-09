#!/usr/bin/python3
""" Module that hosts the Rectangle class """
from models.base import Base



class Rectangle(Base):
    """ Class Rectangle which inherits from base """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        return self.width * self.height

    def display(self):
        if self.y:
            for a in range(self.y):
                print('')
        for i in range(self.height):
            if self.x:
                for b in range(self.x):
                    print(' ', end='')
            for j in range(self.width):
                print('#', end='')
            print('')

    def update(self, *args, **kwargs):
        selves = ['id', 'width', 'height', 'x', 'y']
        if args:
            for a in range(0, len(args)):
                setattr(self, selves[a], args[a])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {'id': self.id, 'width': self.width, 'width': self.width,
                     'height': self.height, 'x': self.x, 'y': self.y}

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) is not int:
            raise TypeError('width must be an integer')
        if val <= 0:
            raise ValueError('width must be > 0')
        self.__width = val


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) is not int:
            raise TypeError('height must be an integer')
        if val <= 0:
            raise ValueError('height must be > 0')
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) is not int:
            raise TypeError('x must be an integer')
        if val < 0:
            raise ValueError('x must be >= 0')
        self.__x = val


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) is not int:
            raise TypeError('y must be an integer')
        if val < 0:
            raise ValueError('y must be >= 0')
        self.__y = val

    def __str__(self):
        return ('[Rectangle] (' + str(self.id) + ') ' + str(self.x) + '/' +
              str(self.y) + ' - ' + str(self.width) + '/' + str(self.height))
