import json
import datetime
import os
import re
import tweepy
import csv

#Variables that contains the user credentials to access Twitter API
import config

access_token = "217383393-lLSrFDHzVJV835JDeanN6rUC8Gab4rYxxlx7BnJ6"
access_token_secret = "L1tfrfvIf42omRbKvaeeJOIo8ckUuvkqdsKLBlA40NPXO"
consumer_key = "GgHtotvzSm39hax7fZX7fH9Ev"
consumer_secret = "qkqEy7y6JIird2Q8MFvnC1afbzHdlJLtpfvGjpVMJNiXW9vzz9"

#username and API key to login Plotly
username='nguyenm'
api_key='0d2bs1bakm'

# Check word contains in a string or not
# If yes -> return True
# Else return False
def word_in_text(word, text):
    match = re.search(word, text)
    if match:
        return True
    return False

def get_all_tweets(screen_name):
    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200, include_rts=False)

    #Get the day of yesterday
    yesterday = (datetime.datetime.now() - datetime.timedelta(1)).strftime("%Y-%m-%d")

    # save most recent tweets
    alltweets.extend(new_tweets)

    # transform the tweepy tweets yesterday into a 2D array that will populate the csv
    outtweets = [
        [tweet.id_str, tweet.user.name, screen_name, tweet.created_at, tweet.retweet_count, tweet.favorite_count,
         tweet.text.encode("utf-8")] for tweet in alltweets if yesterday in str(tweet.created_at)]

    # write the csv
    with open('%s_tweets.csv' % screen_name, 'a') as f:
        writer = csv.writer(f)
        if (not os.path.isfile('%s_tweets.csv' % screen_name)):
            writer.writerow(["id", "name", "screen_name", "created_at", "retweet_count", "favorite_count", "text"])
        writer.writerows(outtweets)
    pass

if __name__ == '__main__':
    # pass in the username of the account you want to download
    for p in config.pre_candidate_keywords:
        get_all_tweets(p)

