#!/usr/bin/python3
"""
This script takes a url, sends a request to the url and
displays the body of the response.
- You have to manage urlilib.error.HTTPError exceptions and print: Error code:
followed by the HTTP status code.
"""
import urllib.request
import urllib.error
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))
