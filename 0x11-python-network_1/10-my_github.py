#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]

    url = 'https://api.github.com/user'
    res = requests.get(url, auth=(username, password))

    if res.status_code == 200:
        user_info = res.json()
        print(user_info.get('id'))
    else:
        print('None')
