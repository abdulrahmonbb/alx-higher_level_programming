#!/usr/bin/python3
"""
This script fetches the url 'https://alx-intranet.hbtn.io/status'
"""
import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    content = requests.get(url)
    body = content.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
