#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given
subreddit.
"""

from requests import get


def recurse(subreddit, hot_list=[], key_w=""):
    """
    doc for recurse
    """
    headers = {"user-agent": "untaljacko"}
    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, key_w)
    try:
        reqs = get(url, headers=headers, allow_redirects=False).json()
        best_ten = reqs["data"]["children"]
        for post in best_ten:
            hot_list.append(post['data']['title'])
        key_w = reqs['data']['after']
        if key_w:
            recurse(subreddit, hot_list, key_w)
        return (hot_list)
    except Exception:
        return ("None")
