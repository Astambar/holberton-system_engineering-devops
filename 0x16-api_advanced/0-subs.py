#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    The number_of_subscribers function returns the number
    of subscribers for a given subreddit.
       If the subreddit does not exist, it returns 0.

    :param subreddit: Specify the subreddit to be queried
    :return: The number of subscribers to a specific subreddit
    :doc-author: Trelent
    """

    responseIsReq = requests.get("https://www.reddit.com/r/{}/about.json".
                                 format(subreddit),
                                 headers={'User-Agent': 'Holberton'})

    if responseIsReq.status_code == 404:
        return 0

    return responseIsReq.json()["data"]["subscribers"]
