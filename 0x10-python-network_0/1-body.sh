#!/bin/bash
# Bash script that displays the size of the body of the response
curl -X GET -sI "$1" | grep -i "Content-length" | awk '{print $2}'
