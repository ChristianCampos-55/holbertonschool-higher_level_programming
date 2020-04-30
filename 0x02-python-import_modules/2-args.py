#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    num = len(argv)-1
    text = 'arguments'
    if num == 1:
        print('1 {:s}:'.format(text[0:8]))
    elif num > 1:
        print('{:d} {:s}:'.format(num, text))
    else:
        print('0 {:s}.'.format(text))

    for i in range(1, len(argv)):
        print('{:d}: {}'.format(i, argv[i]))
