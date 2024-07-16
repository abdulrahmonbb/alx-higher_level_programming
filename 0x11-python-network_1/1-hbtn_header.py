#!/usr/bin/python3
"""
This script sends a request to a url and displays the value
of X-Request-Id variable found in the header of the response.
"""

from sys import argv
from urllib.request import Request
from urllib.request import urlopen

url = argv[1]

if __name__ == '__main__':
    request = Request(url)
    with urlopen(request) as response:
        request_id = response.info().get('X-Request-Id')
        print(request_id)
