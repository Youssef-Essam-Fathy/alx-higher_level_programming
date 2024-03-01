#!/usr/bin/python3
"""
Time for an interview!
"""
import requests
from sys import argv

if __name__ == "__main__":
    repo_name = argv[1]
    owner_name = argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:  # Get the first 10 commits
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
