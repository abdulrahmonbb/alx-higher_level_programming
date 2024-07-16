#!/usr/bin/python3
"""
This script takes a url, sends a POST request to the passed url
with the email as the parameter, and finally displays
the body of the response.
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    r = requests.post(url, data={'email': argv[2]})
    body = r.text
    print(body)
