#!/usr/bin/python3
""" Class Square """


class Square:
    """ definition of size method, with excepted edge cases """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """ set size getter """
    @property
    def size(self):
        return self.__size

    """ set size setter (yeah, try saying that three times) """
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    """ setting position getter """

    @property
    def position(self):
        return self.__position

    """ setting position setter """
    @position.setter
    def position(self, value):
        if (type(value) != tuple or len(value) != 2):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif (type(value[0]) != int or type(value[1]) != int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise ValueError('position must be a tuple of 2 positive integers')

    """ method to get area of Square """
    def area(self):
        return self.__size ** 2

    """ method to print Square size * length with '#' and ' '
        with position into account

    """
    def my_print(self):
        if self.__size > 0:
            if self.__position[1] > 0:
                for i in range(self.__position[1]):
                    print()
            for x in range(self.__size):
                for y in range(self.__position[0]):
                    print(' ', end='')
                for z in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
