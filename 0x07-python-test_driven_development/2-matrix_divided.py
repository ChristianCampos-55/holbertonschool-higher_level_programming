#!/usr/bin/python3
""" Module that hosts matrix_divided function. """


def matrix_divided(matrix, div):
    """ Function that divides two diferent lists (matrix)
        by a specific number (div) """

    type_error = ('matrix must be a matrix (list of lists) of integers/floats')
    len_error = ('Each row of the matrix must have the same size')

    if len(matrix) < 2:
        raise IndexError('not enough lists to divide')

    if type(matrix) is not list:
        raise TypeError(mat_error)

    for x in matrix:
        if len(x) is not len(matrix[0]):
            raise TypeError(len_error)

        for y in x:
            if type(y) not in[int, float]:
                raise TypeError(mat_error)


    if type(div) not in[int, float]:
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(i/div, 2) for i in x] for x in matrix]
