#!/usr/bin/python3
"""A function that queries the Reddit API and
returns the number of total subscribers for
a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """This is the function as previously described"""
    if subreddit is None or not subreddit or not isinstance(subreddit, str):
        return None
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Custom User-Agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException as err:
        return 0
