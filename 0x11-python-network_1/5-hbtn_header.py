#!/usr/bin/python3
"""Requests header info from a URL passed as arg"""
from sys import argv
import requests

if __name__ == '__main__':
    resp = requests.get(argv[1])
    print(resp.headers.get('X-Request-ID'))
