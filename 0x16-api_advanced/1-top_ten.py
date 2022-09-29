#!/usr/bin/python3
""" function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for
a given subreddit."""
import json
import requests
import sys


def top_ten(subreddit):

    url = 'https://www.reddit.com/r/[subreddit]/hot.json'.format(subreddit)
    header = {'User-agent': 'Xavier Perez'}
    size_limit = {"limit": 10}
    r = requests.get(url, params=size_limit, headers=header).json()
    child = r.get('data', {}).get('children', None)
    if child:
        for results in child:
            print(results.get('data').get('tiltle'))
    else:
        print(None)
