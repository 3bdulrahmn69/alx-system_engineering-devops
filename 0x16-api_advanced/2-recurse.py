#!/usr/bin/python3
"""
2-recurse
"""
import requests


def recurse(subreddit, hot_list=[], after='', count=0):
    """queries the Reddit API and returns a list containing the
    titles of all hot articles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'linux:com.myapp:v.1 (by /u/aaorrico)'}
    params = {'after': after, 'count': count, 'limit': 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    results = response.json().get('data')
    after = results.get('after')
    count += results.get('dist')
    for child in results.get('children'):
        hot_list.append(child.get('data').get('title'))

    if after is None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
