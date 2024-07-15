#!/bin/bash
# This script displays the response size in bytes of the request to a url
echo $(curl -s -o /dev/null -w "%{size_download}" "$1")
