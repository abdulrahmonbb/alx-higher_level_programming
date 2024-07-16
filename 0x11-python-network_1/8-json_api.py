#!/usr/bin/python3
"""
The python script takes in a letter and sends a post request to
'http://0.0.0.0:5000/search_user' with the letter as a
parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 2:
        r = requests.post(url, data={"q": argv[1]})
    else:
        r = requests.post(url, data={"q": ""})
    try:
        if r.json() == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.json().get("id"), r.json().get("name")))
    except requests.exceptions.RequestException:
        print("Not a valid JSON")
