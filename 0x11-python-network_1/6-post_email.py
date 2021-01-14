#!/usr/bin/python3
"""Takes URL & Email, sends req to URL with mail as param, shows response"""
import sys
import requests

if __name__ == '__main__':
    req = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(req.text)
