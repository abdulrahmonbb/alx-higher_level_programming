#!/bin/bash
# This script displays the response (of GET request to the url) body with a header variable.
curl -sX GET $1 -H "X-School-User-Id: 98" -L 
