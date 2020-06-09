#!/usr/bin/python3
""" Method that hosts the class square """


from models import rectangle
from models.rectangle import Rectangle

class Square(Rectangle):
    """ class that defines a Square inheriting from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ('[Square] (' + str(self.id) + ') ' + str(self.x) + '/' +
                str(self.y) + ' - ' + str(self.width))
