#!/usr/bin/python3
"""Display response of requested URL"""
import requests
import sys

if __name__ == '__main__':
    to_print = requests.get(sys.argv[1])
    if to_print.status_code >= 400:
        print('Error code:', to_print.status_code)
    else:
        print(to_print.text)
