#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    ptr_hid = dir(hidden_4)
    for i in ptr_hid:
        if i[:2] != '__':
            print(i)
