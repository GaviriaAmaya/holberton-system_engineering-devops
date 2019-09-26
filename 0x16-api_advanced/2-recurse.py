#!/usr/bin/python3
'recurse reddit API'
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    api = 'https://www.reddit.com/r/{}/hot.json?limit'.format(subreddit)
    header = {'User-Agent': 'Judama15'}

    if after:
        api = '{}&after={}'.format(api, after)
        resp = get(api, headers=header)
        if resp.status_code > 200:
            return None
        resp = resp.json()
        children = r['data']['children']
        after = r['data']['after']
        for i in children:
            title = i['data']['title']
            hot_list.append(title)
            if after:
                return recurse(subreddit, hot_list, after)
            return hot_list
