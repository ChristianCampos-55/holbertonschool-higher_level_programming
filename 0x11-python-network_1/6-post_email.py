#!/usr/bin/python3
"""Takes in a URL and Email, sends req to URL with mail as param, shows response"""
from sys import argv
import requests

if __name__ == '__main__':
    req = requests.post(argv[1], {'email': argv[2]})
    print(req.text)
