import json
import datetime
import os
import re
import tweepy
import csv
import TweetsVisualizationDaily as preDaily
import TweetsVisualizationMonthly as preMonthly
import VicePreTweetsVisualizationDaily as viceDaily
import VicePreTweetsVisualizationMonthly as viceMonthly

#Variables that contains the user credentials to access Twitter API
import config

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
    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
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
        [tweet.id_str, tweet.user.name.encode("utf-8"), screen_name, tweet.created_at, tweet.retweet_count, tweet.favorite_count,
         tweet.text.encode("utf-8")] for tweet in alltweets if yesterday in str(tweet.created_at)]
    # write the csv
    with open('%s_tweets.csv' % screen_name, 'a', newline='') as f:
        writer = csv.writer(f)
        if (os.stat('%s_tweets.csv' % screen_name).st_size == 0):
            writer.writerow(["id", "name", "screen_name", "created_at", "retweet_count", "favorite_count", "text"])
        writer.writerows(outtweets)
    pass

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))

    # pass in the username of the account you want to download
    #for p in config.pre_candidate_keywords:
     #   get_all_tweets(p)

    #for p in config.vicepre_candidate_keywords:
     #   get_all_tweets(p)

    preDaily.main()
    preMonthly.main()
    viceDaily.main()
    viceMonthly.main()


