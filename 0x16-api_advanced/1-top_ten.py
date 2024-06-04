#!/usr/bin/python3
"""A function that queries the Reddit API and
prints the titles of the first 10 hot posts
listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Queries the Reddit API for the top 10 hot posts
    of a subreddit and prints their titles

    Args:
    subreddit: The name of the subreddit to query.

    Returns:
    None
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'My Reddit App (v1.0)'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            if 'data' not in data or 'children' not in data['data']:
                print("Subreddit {} not found.".format(subreddit))
                return
            for post in data['data']['children'][:10]:
                print(post['data']['title'])

    except requests.exceptions.RequestException as e:
        print("Error fetching top 10 posts: {}".format(e))
