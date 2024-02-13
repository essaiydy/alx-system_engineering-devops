#!/usr/bin/python3
'''fonction'''
import requests


def number_of_subscribers(subreddit):
    '''Write a function that queries the Reddit API and
    returns the number of subscribers
    (not active users, total subscribers) for a given subreddit'''
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': Mozilla/5.0 (Windows NT 10.0; Win64; x64)
            AppleWebKit/537.36 (KHTML, like Gecko)
            Chrome/58.0.3029.110 Safari/537.3}
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return 0
    dictt = response.json().get("data")
    return(dictt.get("subscribers")
