#!/usr/bin/python3
"""
This script sends a request to a url and displays the value of
a variable found in the header of the response.
"""
import urllib.request
from sys import argv

if __name__ == '__main__':
    """
    takes a url, sends a request and displays
    the value of the X-Request-Id variable.
    """
    with urllib.request.urlopen(argv[1]) as response:
        request_id = response.info().get('X-Request-Id')
        print(request_id)
