#! /usr/bin/env python3
"""
Check that account!

"""

import requests
import json
from twilio.rest import Client
import os
import datetime as dt

now = dt.datetime.now()

def get_tweets():
    TWITTER_BEARER_TOKEN = "fillme"
    query = "from:IAVaccineAlerts"
    tweet_fields = "tweet.fields=author_id"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields
    )

    headers = {"Authorization": "Bearer {}".format(TWITTER_BEARER_TOKEN)}

    response = requests.request("GET", url, headers=headers)

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def send_notice(msg):
    account_sid = "fillme"
    auth_token = "fillme"
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
                body=msg,
                from_='fillme', # should be +1xxxxxxxxxx
                to='fillme'     # should be +1xxxxxxxxxx
            )

    print(message.sid)

def sanity_check(msg):
    """
    Don't oversend, that costs me like 2 cents!
    """
    if (now.timestamp() - os.path.getmtime('notice-sent.txt')) > 3600:
        send_notice(msg)
        with open('notice-sent.txt', 'w+') as f:
            f.write(msg)
    else:
        print("Found town, but message has already been sent in the last hour.")


def main():
    # print(json.dumps(get_tweets(), indent=4, sort_keys=True))

    find_towns = ['fillme']

    for tweet in get_tweets()['data']:
        for town in find_towns:
            if town.lower() in tweet['text'].lower():
                sanity_check(tweet['text'])


if __name__ == "__main__":
    main()