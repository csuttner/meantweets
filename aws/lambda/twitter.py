__author__ = 'evfairchild'
# !/usr/bin/env python
# encoding: utf-8

'''
Twitter only allows access to a users most recent 3240 tweets with this method
Twitter limits the number of requests allowed on free developer accounts.  Please run this script sparingly.

Because of all the Twitter limitations, we may want to consider a JSON web approach down the road.  See here:
https://github.com/Jefferson-Henrique/GetOldTweets-python
'''

import os
import tweepy
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

        return [tweet.text.replace('\n', '') for tweet in tweets]

    def words(self):
        all_words = ' '.join(self.get_tweets()).split(' ')

        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

        with open(os.path.join(__location__,'stopwords.txt'), 'r') as file:
            stopwords = file.read().split('\n')

        words = {}
        for word in all_words:
            if word.lower() not in stopwords:
                words[word] = words.get(word, 0) + 1
            else:
                pass

        # apparently you can sort dicts in Python 3.9
        words = {k: v for k, v in sorted(words.items(), key=lambda item: item[1], reverse=True)}

        unique = set(words)

        return len(unique), words

    def get_image(self):
        return None

    def build_mt_json(self):
        unique, words = self.words()
        data = {"handle": self.handle,
                "tweet_count": self.count,
                "image": self.get_image(),
                "unique_words": unique,
                "words":
                    words
                }

        return data

if __name__ == "__main__":
    print(Twitter('@AOC').data)
