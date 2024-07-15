#!/bin/bash
# This script displays the body of the response of a GET request to the url
echo $(curl -s -X GET "$1")
