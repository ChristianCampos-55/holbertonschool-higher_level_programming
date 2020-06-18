#!/usr/bin/python3
for a in range(0, 9):
    for b in range(a+1, 10):
        if a is 8 and b is 9:
            print('{}{}'.format(a, b))
        else:
            print('{}{}, '.format(a, b), end='')
