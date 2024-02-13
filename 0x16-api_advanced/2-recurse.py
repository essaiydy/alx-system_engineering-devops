#!/usr/bin/python3
"""Contains recurse function"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    '''Write a recursive function that queries the Reddit
    API and returns a list containing the titles of all hot
    articles for a given subreddit. If no results are found
    for the given subreddit, the function should return None.'''
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' +
            'AppleWebKit/537.36 (KHTML, like Gecko)' +
            'Chrome/58.0.3029.110 Safari/537.3'
            }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    hot_list.extend(
            [i.get("data").get("title") for i in results.get("children")])

    return recurse(subreddit, hot_list, after, count) if after else hot_list
