__author__ = 'evfairchild'
# !/usr/bin/env python
# encoding: utf-8

'''
Twitter only allows access to a users most recent 3240 tweets with this method
Twitter limits the number of requests allowed on free developer accounts.  Please run this script sparingly.

Because of all the Twitter limitations, we may want to consider a JSON web approach down the road.  See here:
https://github.com/Jefferson-Henrique/GetOldTweets-python
'''

import json
import tweepy
import argparse
from secrets import *


class Twitter(object):
    def __init__(self, handle, count=10):
        self.handle = handle
        self.count = count

        # authorize twitter, initialize tweepy
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        self.api = tweepy.API(auth)

        self.data = self.build_mt_json()

    def get_tweets(self):
        tweets = self.api.user_timeline(screen_name=self.handle, count=self.count)

        # transform the tweepy tweets into a 2D array that will populate the csv
        return [tweet.text.replace('\n', '') for tweet in tweets]

    def words(self):
        all_words = ' '.join(self.get_tweets()).split(' ')

        with open('stopwords.txt', 'r') as file:
            stopwords = file.read().split('\n')

        words = []
        word_counts = {}
        for word in all_words:
            if word.lower() not in stopwords:
                word_counts[word] = word_counts.get(word, 0) + 1
            else:
                pass

        # apparently you can sort dicts in Python 3.9
        word_counts = {k: v for k, v in sorted(word_counts.items(), key=lambda item: item[1], reverse=True)}

        for word in word_counts.keys():
            words.append(
                {
                    "word": word,
                    "count": word_counts[word],
                    "score": word_counts[word]
                }
            )

        return len(words), words

    def build_mt_json(self):
        unique, words = self.words()
        data = {
            "handle": self.handle,
            "tweet_count": self.count,
            "unique_words": unique,
            "words": words
        }

        return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', '-u', type=str)
    args = parser.parse_args()
    clay = '@ClaySuttner'
    potus = '@POTUS'
    print(type(Twitter(potus).data))
