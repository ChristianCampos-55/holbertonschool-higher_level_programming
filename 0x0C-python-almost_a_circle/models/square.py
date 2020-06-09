#!/usr/bin/python3
""" Module that hosts the square Class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class sqaure which inherits from rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ class constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter for size with Rectangle's width """
        return self.width

    @size.setter
    def size(self, val):
        """ setter for size with Rectangle's width """
        self.width = val
        self.height = val

    def __str__(self):
        """ re-resignification of string method """
        return ('[Square] (' + str(self.id) + ') ' + str(self.x) + '/' +
                str(self.y) + ' - ' + str(self.width))
