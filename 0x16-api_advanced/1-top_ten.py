#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the
    first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'linux:com.myapp:v.1 (by /u/aaorrico)'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return 0
    results = response.json().get('data')
    for child in results.get('children'):
        print(child.get('data').get('title'))
