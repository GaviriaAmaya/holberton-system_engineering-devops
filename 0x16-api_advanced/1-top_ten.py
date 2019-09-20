#!/usr/bin/python3
'Titles of the first ten hot posts!'
from requests import get


def top_ten(subreddit):
    if type(subreddit) is not str:
        return 0

    api = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = {'user-agent': 'Judama15'}
    resp = get(api, headers=header, allow_redirects=False)

    if resp.status_code != 200:
        return None

    else:
        jsf = resp.json()['data']['children']

        return '\n'.join([jsf[i]['data']['title']for i in range(10)])
