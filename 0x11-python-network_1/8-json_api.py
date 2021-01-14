#!/usr/bin/python3
"""Sends a POST request with a letter as parameter"""
import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    letter = ''
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    data = {'q': letter}
    requested = requests.post(url, data)
    try:
        js_on = requested.json()
        if js_on == {}:
            print('No result')
        else:
            print('[{}] {}'.format(result.get('id'), result.get('name')))
    except:
        print('Not a valid JSON')
