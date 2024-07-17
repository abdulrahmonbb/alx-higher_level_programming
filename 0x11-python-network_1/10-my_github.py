#!/usr/bin/python3
"""
This script takes github credentials (username and password)
and uses the github api to display the id.
"""
import requests
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    url = f'https://api.github.com/users/{username}'
    headers = {'Authorization': f"Basic {(username + ':' + password).encode().hex()}"}

    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        print(r.json().get('id'))
    except requests.exceptions.RequestException:
        pass

