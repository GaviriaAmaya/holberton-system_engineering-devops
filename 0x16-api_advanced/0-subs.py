#!/usr/bin/python3
'Returns the number of subscribers from the Reddit API'
from requests import get


def number_of_subscribers(subreddit):

    if type(subreddit) is str:
        api = "https://www.reddit.com/r/{}/about/.json".format(subreddit)
        header = {'user-agent': 'Judama15'}
        subs = get(api, headers=header, allow_redirects=False)

        if subs.status_code is 200:
            return subs.json()['data']['subscribers']
        else:
            return 0

    else:
        return 0
