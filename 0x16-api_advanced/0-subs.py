#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given
subreddit. If an invalid subreddit is given, the function should return 0.
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    doc for number of subscribers of reddit
    """
    headers = {"user-agent": "untaljacko"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    try:
        reqs = get(url, headers=headers).json()
        counter = reqs["data"]["subscribers"]
        return (counter)
    except Exception:
        return 0
