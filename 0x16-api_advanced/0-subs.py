#!/usr/bin/python3
"""function that queries the Reddit API
and returns the number of subscribers"""
import json
import requests
import sys


def number_of_subscribers(subreddit):

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-agent': 'Custom Agent',
              'From': 'xnator9@gmail.com'}
    request = requests.get(url, headers=header)
    request_json = json.loads(request.text)

    if request.status_code == 404:
        return 0
    else:
        return request_json['data']['subscribers']
