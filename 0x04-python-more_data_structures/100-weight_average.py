#!/usr/bin/python3
def weight_average(my_list=[]):
    n, d = 0, 0
    if my_list:
        for i in my_list:
            n += i[0] * i[1]
            d += i[1]
        return n / d
