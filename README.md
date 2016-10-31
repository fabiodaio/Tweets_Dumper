# Tweets_Dumper
Python script to collect tweets from Twitter


__userTweets_to_sqlite.py__:
* collects the latest tweets from a specific Twitter user.

__streamTweets_to_sqlite.py__:
* collects streams of tweets filtered based on pre-specified words.


Requirements:
* Install tweepy
* Create a Twitter app at https://apps.twitter.com/ to get credentials

How to run:
* Pass twitter username string as argument to _get_all_tweets()_ in _userTweets_to_sqlite.py_
* Pass tuple of keywords strings to be filtered as argument to _get_tweets_stream()_ in _streamTweets_to_sqlite.py_
* Run command line: `$ python xxxTweets_to_sqlite`


To know what the collected data looks like before being written to the database, check examples of outputs from Tweepy framework in _tweets_structure_ folder.
