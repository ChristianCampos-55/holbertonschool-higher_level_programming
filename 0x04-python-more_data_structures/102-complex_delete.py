#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key_curr, val_curr in dict(a_dictionary).items():
        if value is val_curr:
            a_dictionary.pop(key_curr)
    return a_dictionary
