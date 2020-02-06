#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given
subreddit. If an invalid subreddit is given, the function should return 0.
"""

from requests import get


def recurse(subreddit, hot_list=[], key1=""):
    """
    doc for top_ten posts of reddit
    """
    headers = {"user-agent": "untaljacko"}
    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, key1)
    try:
        reqs = get(url, headers=headers, allow_redirects=False).json()
        best_ten = reqs["data"]["children"]
        for post in best_ten:
            hot_list.append(post['data']['title'])
        key1 = reqs['data']['after']
        if key1:
            recurse(subreddit, hot_list, key1)
        return (hot_list)
    except Exception:
        return ("None")
