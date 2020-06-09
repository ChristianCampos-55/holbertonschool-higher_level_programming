#!/usr/bin/python3
""" Module that hosts the square Class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class sqaure which inherits from rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ re-resignification of string method """
        return ('[Square] (' + str(self.id) + ') ' + str(self.x) + '/' +
                str(self.y) + ' - ' + str(self.width))
