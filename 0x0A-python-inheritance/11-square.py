#!/usr/bin/python3
""" Method that hosts class Square, who inherits from Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """method that validates size and inherits area from
       rectangle """

    def __init__(self, size):
        self.integer_validator('size', size)
        super().__init__(size, size)

    def __str__(self):
        return '[Square] {}/{}'.format(self.__size, self.__size)
