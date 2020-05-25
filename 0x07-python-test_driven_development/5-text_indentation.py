#!/usr/bin/python3
""" Module that hosts text_indentation function """


def text_indentation(text):
    """ Function that prints the 'text' received, but
        adds two '\n' after each '.', '?' or ':'.
    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    new_line = ('.', '?', ':')

    for i in range(len(text)):
        if text[i] is ' ' and text[i-1] in new_line:
            continue
        print(text[i], end='')
        if text[i] in new_line:
            print(end='\n\n')
