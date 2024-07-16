#!/usr/bin/python3
"""
This script fetches a url using urllib
"""
from urllib.request import urlopen
from urllib.request import Request

url = 'https://alx-intranet.hbtn.io/status'

if __name__ == '__main__':
    request = Request(url)
    with urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
