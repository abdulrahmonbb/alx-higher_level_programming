#!/usr/bin/python3
"""
This script takes a url, sends a request to the url and
displays the value of the variable X-Request-Id
in the response header
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    content = requests.get(url)
    request_id = content.headers.get('X-Request-Id')
    print("{}".format(request_id))
