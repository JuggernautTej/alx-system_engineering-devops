#!/usr/bin/python3
""" A recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles
for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively fetches titles of all hot articles for a subreddit using
    pagination.

    Args:
    subreddit: The name of the subreddit to query.
    hot_list: (Optional) A list to accumulate titles across recursive
    calls (defaults to []).

    Returns:
    A list containing titles of all hot articles or None if the
    subreddit is invalid.
    """
    if subreddit is None or not subreddit or not isinstance(subreddit, str):
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My Reddit App (v1.0)'}
    query_params = {'after': after, 'count': count, 'limit': 100}
    try:
        response = requests.get(url, headers=headers,
                                params=query_params, allow_redirects=False)

        if response.status_code != 200:
            return None

        data = response.json().get('data')
        after = data.get('after')
        count += data.get('dist')
        children = data.get('children')

        for kid in children:
            hot_list.append(kid.get('data').get('title'))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list

    except Exception:
        return None
