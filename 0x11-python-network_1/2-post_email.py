#!/usr/bin/python3
"""Sends a POST request with email as param and outputs response"""

from urllib import parse, request
import sys

if __name__ == '__main__':
    info = parse.urlencode({'email': sys.argv[2]}).encode()
    with request.urlopen(sys.argv[1], info) as response:
        print(response.read().decode('utf-8'))
