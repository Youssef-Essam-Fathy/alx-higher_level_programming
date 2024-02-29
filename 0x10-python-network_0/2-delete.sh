#!/bin/bash
#Bash script that takes in a URL, sends a DELETE request to the URL, and displays the size of the body of the response
curl -sX DELETE "$1"  
