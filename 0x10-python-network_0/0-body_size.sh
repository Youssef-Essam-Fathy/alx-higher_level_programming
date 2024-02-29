#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
URL=$1
curl -s "$URL" | grep -i "Content-length" | awk '{print $2}'