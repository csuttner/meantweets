# !/usr/bin/env python
# encoding: utf-8

'''
Twitter only allows access to a users most recent 3240 tweets with this method
This script batch queries the Twitter API 200 tweets at a time.
Twitter limits the number of requests allowed on free developer accounts.  Please run this script sparingly.

Because of all the Twitter limitations, we may want to consider a JSON web approach down the road.  See here:
https://github.com/Jefferson-Henrique/GetOldTweets-python

For additional Tweet object attributes see:
https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object.html
'''

import tweepy
import csv
import argparse
from secrets import *


def all_tweets(screen_name):

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    alltweets = []

    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        # print "getting tweets before %s" % (oldest)
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))

    # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.text.encode("utf-8")] for tweet in alltweets]  # we can request tons of different attributes
    # print(outtweets[0:100])

    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        # writer.writerow(["id", "created_at", "text"])
        writer.writerows(outtweets)
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', '-u', type=str)
    args = parser.parse_args()
    all_tweets(args.username)
