import pymongo
import tweepy

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def get_tweets_stream(filters):
    filters_array = list(filters)

    my_auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    my_auth.set_access_token(access_key, access_secret)
    api = tweepy.API(my_auth)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener = MyStreamListener())

    print(filters_array)
    # myStream.filter(track=['python'])
    myStream.filter(track = filters_array)

def save_tweets_to_db(data):
    #connect to MongoDB database
    client = pymongo.MongoClient() #defaults to localhost at port 27017

    #assign the database named Stream Tweets
    db = client['Stream_Tweets']

    #assign the collection (table) object
    db['stream_tweets']

    #insert
    result = db.stream_tweets.insert_one(data._json)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print("GETTING DATA......")
        print(status.text) # print tweets text to screen
        save_tweets_to_db(status)

    def on_error(self, status_code):
        print("ERROR!!!!!!")
        if status_code == 420:
            #returning False in on_data disconnects the stream
            print('Error 420: DISCONNECTING THE STREAM')
            return False

get_tweets_stream(('#sad', 'good', 'love', '#happy'))
