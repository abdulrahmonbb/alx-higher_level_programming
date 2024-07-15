#!/bin/bash
# This script sends a POST request to a url and displays the response
curl -sX POST $1 -d "email=test@gmail.com&subject=I will always be here for PLD" -L
