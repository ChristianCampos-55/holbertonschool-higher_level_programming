#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
opn = [add, sub, mul, div]
opr = ['+', '-', '*', '/']
for i in range(0, 4):
    print('{} {} {} = {}'.format(a, opr[i], b, opn[i](a, b)))

if __name__ == '__main__':
    add(a, b)
    sub(a, b)
    mul(a, b)
    div(a, b)
