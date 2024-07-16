#!/usr/bin/python3
"""
This script takes a url, sends a request to the url
and displays the body of the response.
- If the HTTP status code is greater than 400, print
`Error code:` followed by the value of the HTTP status
code.
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
