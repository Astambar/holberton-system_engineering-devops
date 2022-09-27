#!/usr/bin/python3
"""
queries the Reddit API
"""
import requests


def add_value(hot_list, data, count=0):
    """
    The add_value function takes a list and a dictionary.
    It then iterates through the
    dictionary to find all of the titles of hot posts on Reddit.
    The function returns a list
    of all of these titles.

    :param hot_list: Store the titles of the hot posts
    :param data: Store the data from the json file
    :param count=0: Keep track of the index position in the list
    :return: A list of the titles of the hot posts on r/askreddit
    :doc-author: Trelent
    """

    try:
        hot_list.append(data["children"][count]["data"]["title"])
    except IndexError:
        return hot_list
    count += 1

    return add_value(hot_list, data, count)


def recurse(subreddit, hot_list=[], after=None):
    """
    The recurse function takes a subreddit and returns the list of titles
    of all hot articles for that subreddit.
    If no results are found, it returns None.

    :param subreddit: Specify the subreddit to be searched
    :param hot_list=[]: Store the data from the api call
    :param after=None: Get the next page of results
    :return: A list of dictionaries
    :doc-author: Trelent
    """
    responseIsReq = requests.get(
        "https://www.reddit.com/r/" + subreddit + "/hot.json",
        headers={'User-Agent': 'Holberton'},
        params={'after': after}
    )

    if responseIsReq.status_code == 404:
        return None

    data = responseIsReq.json()["data"]
    hot_list = add_value(hot_list, data)
    if data["after"] is None:
        return hot_list

    return recurse(subreddit, hot_list, data["after"])
