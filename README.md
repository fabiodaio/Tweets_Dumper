# Tweets_Dumper
Python script to collect tweets from Twitter


__userTweets_to_sqlite.py__:
* collects the latest tweets from a specific Twitter user.

__streamTweets_to_sqlite.py__:
* collects streams of tweets filtered based on pre-specified words.


__Requirements:__
* Install tweepy
* Create a Twitter app at https://apps.twitter.com/ to get credentials

__How to run:__
* Pass twitter username string as argument to `get_all_tweets()` in _userTweets_to_sqlite.py_
* Pass tuple of keywords strings to be filtered as argument to `get_tweets_stream()` in _streamTweets_to_sqlite.py_
* Run command line: `$ python xxxTweets_to_sqlite`


To know what the collected data looks like before being written to the database, check examples of outputs from Tweepy framework in _tweets_structure_ folder.
