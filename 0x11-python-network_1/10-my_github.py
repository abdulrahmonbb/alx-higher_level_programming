#!/usr/bin/python3
"""
This script takes github credentials (username and password)
and uses the github api to display the id.
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/user/'
    username = argv[1]
    password = argv[2]

    r = requests.get(url, auth=(argv[1], argv[2])
    try:
        print(r.json().get('id')
    except
