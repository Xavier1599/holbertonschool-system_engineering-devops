#!/usr/bin/python3
""" function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for
a given subreddit."""
import json
import requests
import sys


def top_ten(subreddit):

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-agent': 'Custom Agent'}
    size = {"limit": 10}
    r = requests.get(url, params=size, headers=headers).json()
    child = r.get('data', {}).get('children', None)
    if child:
        for results in child:
            print(results.get('data').get('title'))
    else:
        print(None)
