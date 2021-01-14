#!/usr/bin/python3
"""Sends a POST request with a letter as parameter"""
import requests
import sys

if __name__ == '__main__':
    data = {'q': ''}
    url = "http://0.0.0.0:5000/search_user"
    requested = requests.post(url, data)
    if len(sys.argv) > 1:
        user = sys.argv[1]
    try:
        js_on = req.json()
        if js_on == {}:
            print('No result')
        else:
            print('[{}] {}'.format(result.get('id'), result.get(name)))
    except:
        print('Not a valid JSON')
