#!/bin/bash
# This script displays all the HTTP methods that a server will accept
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
