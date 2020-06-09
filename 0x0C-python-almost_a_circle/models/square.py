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

    def update(self, *args, **kwargs):
        selves = ['id', 'size', 'x', 'y']
        if args is not None and len(args) !=0:
            for a in range(0, len(args)):
                setattr(self, selves[a], args[a])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
