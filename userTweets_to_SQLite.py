import sqlite3
import tweepy

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def get_all_tweets(screen_name):
    # screen_name should be the twitter username of whom we want to collect data
    # Twitter only allows access to a users most recent 3000 tweets with this method

	#authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []

	#make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)

	#save most recent tweets
    alltweets.extend(new_tweets)

	#save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)

		#all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

		#save most recent tweets
        alltweets.extend(new_tweets)

		#update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print "...%s tweets downloaded so far" % (len(alltweets))

    #transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text, str(tweet.place)] for tweet in alltweets] #tweet.text.encode("utf-8")

    #connect to SQLite database
    conn = sqlite3.connect('example %s.db' % screen_name)
    #conn.text_factory = str #necessary to be able to store utf-8 strings in db

    #create a cursor so that we can execute SQL commands
    c = conn.cursor()
    #create table
    c.execute("CREATE TABLE tweets(Tweet_ID, Tweet_Date, Tweet_Text, Tweet_Place)")

    #insert a row of data
    for row in outtweets:
        c.execute('INSERT INTO tweets VALUES (?, ?, ?, ?)', row)
    #save (commit) the changes
    conn.commit()
    # Close the connection if we are done with it.
    # Be sure any changes have been committed or they will be lost.
    conn.close()

get_all_tweets('realDonaldTrump')
