#!/usr/bin/python3
"""Displays the ID of GitHub with credentials passed as args"""
import sys
import requests

if __name__ == '__main__':
    to_print = requests.get('https://api.github.com/user',
                            auth=(sys.argv[1], sys.argv[2]))
    print(to_print.json().get('id'))
