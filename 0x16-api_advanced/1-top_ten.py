#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given
subreddit. If an invalid subreddit is given, the function should return 0.
"""

from requests import get


def top_ten(subreddit):
    """
    doc for top_ten posts of reddit
    """
    headers = {"user-agent": "untaljacko"}
    url = "https://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    try:
        reqs = get(url, headers=headers, allow_redirects=False).json()
        best_ten = reqs["data"]["children"]
        for post in best_ten:
            print(post['data']['title'])
    except Exception:
        print("None")
