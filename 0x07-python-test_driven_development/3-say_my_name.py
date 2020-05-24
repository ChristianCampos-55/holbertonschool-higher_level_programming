#!/usr/bin/python3
""" Module that hosts the say_my_name function """


def say_my_name(first_name, last_name=""):
    """ Function that receives two parameters (first_name
        and last_name) and prints them. Both must be srings
    """

    if not first_name and not last_name:
        raise TypeError('The function needs at least one valid value')

    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')
    else:
        print('My name is {} {}'.format(first_name, last_name))
