#!/usr/bin/python3
"""
This script takes GitHub credentials (username and password)
and uses the GitHub API to display the id.
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    username = argv[1]
    password = argv[2]
    r = requests.get(url, auth=(username, password))
    try:
        print(r.json().get('id'))
    except requests.exceptions.RequestException:
        pass
