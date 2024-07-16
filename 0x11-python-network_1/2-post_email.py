#!/usr/bin/python3
"""
This script takes a url and an email, sends a POST request
to the passed url with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    data = {'email': argv[2]}

    data_encoded = urllib.parse.urlencode(data)
    data_encoded = data_encoded.encode('ascii')

    req = urllib.request.Request(url, data_encoded)
    with urllib.request.urlopen(req) as response:
        response_data = response.read().decode('utf-8')
        print(response_data)
