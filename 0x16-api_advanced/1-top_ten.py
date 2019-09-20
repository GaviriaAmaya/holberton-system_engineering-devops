#!/usr/bin/python3
'Titles of the first ten hot posts!'
from requests import get


def top_ten(subreddit):

    api = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = {'user-agent': 'Judama15'}
    parq = {'limit': 10}
    resp = get(api, headers=header, allow_redirects=False, params=parq)

    if resp.status_code == 200:
        jsf = resp.json().get('data').get('children')
        for js in jsf:
            print(js.get('data').get('title'))
    else:
        print("None")
