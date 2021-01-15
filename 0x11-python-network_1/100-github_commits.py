#!/usr/bin/python3
"""Use Github API to list 10 last commits from a specific user"""
import requests
import sys


if __name__ == '__main__':
        try:
                get = requests.get('https://api.github.com/repos/{}/{}/commits'
                                   .format(sys.argv[2], sys.argv[1]))
                j_on = get.json()
                for i in range(0, 10):
                        print('{}: {}'.format(j_on[i].get('sha'), j_on[i].get(
                                'commit').get('author').get('name')))
        except:
                pass
