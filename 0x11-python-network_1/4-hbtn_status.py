#!/usr/bin/python3
import requests
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    try:
        response = requests.get(url)
        print("Body response:")
        print("\t- type:", type(response.text))
        print("\t- content:", response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
