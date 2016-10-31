import sqlite3
import tweepy

DATABASE_NAME = 'example stream.db'

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def get_tweets_stream(filters):
    #connect to SQLite database
    conn = sqlite3.connect(DATABASE_NAME)

    #create a cursor so that we can execute SQL commands
    c = conn.cursor()
    #create table
    c.execute("CREATE TABLE tweets(Tweet_ID, Tweet_Date, Tweet_Text, Tweet_Place)")
    #save (commit) the changes
    conn.commit()
    # Close the connection if we are done with it.
    # Be sure any changes have been committed or they will be lost.
    conn.close()

    filters_array = list(filters)

    my_auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    my_auth.set_access_token(access_key, access_secret)
    api = tweepy.API(my_auth)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener = MyStreamListener())

    print(filters_array)
    myStream.filter(track = filters_array)

def save_tweets_to_db(data):
    row = [data.id_str, data.created_at, data.text, str(data.place)]
    #connect to SQLite database
    conn = sqlite3.connect(DATABASE_NAME)
    #create a cursor so that we can execute SQL commands
    c = conn.cursor()
    #create table
    c.execute('INSERT INTO tweets VALUES (?, ?, ?, ?)', row)
    #save (commit) the changes
    conn.commit()
    # Close the connection if we are done with it.
    # Be sure any changes have been committed or they will be lost.
    conn.close()

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

get_tweets_stream(('#sad', 'good', 'love', '#happy')) # specify words to filter here!
