#!/usr/bin/python3

"""
Advanced API Count
"""

import requests


def count_words(subreddit, word_list, dictWord={}, after=None):
    """
    The count_words function takes a subreddit and a list of words as input.
    It returns the number of times each word in
    the list appears on that subreddit's hot page.
    The function will make at most 10 calls to reddit's
    API per invocation, and will sleep for two seconds after each call.

    :param subreddit: Specify the subreddit to be searched
    :param word_list: Store the words that
    will be counted in the title of each post
    :param dictWord={}: Store the words and their
    corresponding number of occurences in a dictionary
    :param after=None: Get the next page of results
    :return: A dictionary with the word and number
    of times it appears in a title for a given subreddit
    :doc-author: Trelent
    """
    if subreddit is None:
        print(None)
    URL = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'Holberton User Agent 1.0',
        'From': 'leuchartjason@gmail.com',
    }
    response = requests.get(
        URL,
        headers=headers,
        params={'after': after, 'limit': 10}
    )
    if response.status_code == 404:
        return
    data = response.json()
    allHost = data.get("data", {}).get("children", None)
    after = data.get("data", {}).get("after", None)
    for hotPost in allHost:
        title = hotPost.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            if word.lower() in title:
                numIteration = sum(word.lower() == w for w in title)
                if word.lower() not in dictWord.keys():
                    dictWord[word.lower()] = numIteration
                else:
                    dictWord[word.lower()] += numIteration
    if after is None:
        if len(dictWord) != 0:
            dictWord = sorted(dictWord.items(),
                              key=lambda keyvalue: (-keyvalue[1], keyvalue[0]))
            for key, value in dictWord:
                print('{}: {}'.format(key, value))
        return
    return count_words(subreddit, word_list, dictWord, after)
