#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to 
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        json_res = res.json()
        if json_res:
            print("[{}] {}".format(json_res['id'], json_res['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
