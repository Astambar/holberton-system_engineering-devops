#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    The top_ten function takes a subreddit as
    an argument and returns the top 10
    hot posts for that subreddit.
    If the subreddit does not exist, it returns None.

    :param subreddit: Pass the name of the subreddit to be analyzed
    :return: The titles of the first 10 hot posts listed for a given subreddit
    :doc-author: Trelent
    """

    responseIsReq = requests.get(
        "https://www.reddit.com/r/" + subreddit + "/hot.json",
        headers={'User-Agent': 'Holberton'}
    )
    tmpPrinter = ""
    if responseIsReq.status_code == 404:
        tmpPrinter += "None\n"
    else:
        data = responseIsReq.json()["data"]["children"]
        for title in data[:10]:
            tmpPrinter += title["data"]["title"]+"\n"
    print(tmpPrinter)
