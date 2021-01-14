#!/usr/bin/python3
"""Use Github API to list 10 last commits from a specific user"""
import requests
import sys


if __name__ == '__main__':
        to_get = requests.get('https://api.github.com/repos/{}/{}/commits'
                              .format(sys.argv[2], sys.argv[1]))
        js_on = to_get.json()
        for i in range(0, 10):
            print('{}: {}'.format(js_on[i].get('sha'), js_on[i].get('commit')
                                  .get('author').get('name')))
