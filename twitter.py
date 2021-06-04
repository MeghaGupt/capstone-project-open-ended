from configreader import ConfigReader
from datetime import datetime, timedelta
import requests
import pandas as pd
import re
import glob


def clean(tweet):

    whitespace = re.compile(r"\s+")
    web_address = re.compile(r"(?i)http(s):\/\/[a-z0-9.~_\-\/]+")
    #tesla = re.compile(r"(?i)@Tesla(?=\b)")
    user = re.compile(r"(?i)@[a-z0-9_]+")
    tweet = whitespace.sub(' ', tweet)
    tweet = web_address.sub('', tweet)
    tweet = tesla.sub('Tesla', tweet)
    tweet = user.sub('', tweet)

    return(tweet)

#reference doc - https://towardsdatascience.com/sentiment-analysis-for-stock-price-prediction-in-python-bed40c65d178

if __name__ == '__main__':

    configreader = ConfigReader()
    config = configreader.read_config('config.ini','twitter')
    print(config)
    #filename = config['file_name']
    API_KEY =  config['api_key']
    API_SECRET_KEY =  config['api_secret_key']
    #slices = config['slices'].split(",")
    BEARER_TOKEN = config['bearer_token']
    ACCESS_TOKEN = config['access_token']
    ACCESS_SECRET = config['access_token_secret']
    print(BEARER_TOKEN)

    #response = requests.get(
    #'https://api.twitter.com/1.1/search/tweets.json?q=tesla',https://medium.com/geekculture/how-to-get-twitter-data-with-tweepy-4663fbc8b90b
    #headers={
    #    'authorization': 'Bearer '+bearer_token
#})

#Tweepy Package
import tweepy as tw
#Connecting to the API
auth = tw.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
search_words = "#tsla -filter:retweets"


tweet_dataset = pd.DataFrame(columns=['Search Word','Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text'])
counter = 0


config = configreader.read_config('config.ini','alpha_vantage')
filename = config['file_name']
filenames = glob.glob(filename + "*.csv")


search_words = "#tsla -filter:retweets"

for file in filenames:
    df = pd.read_csv(file)
    for index, row in df.iterrows():
        print(row["Code"])
        search_words = "#"+ row["Code"]+" -filter:retweets"
        for tweet in tw.Cursor(api.search, tweet_mode='extended', q=search_words, lang="en").items():
                print('Tweet Downloaded: ', counter)
                appending_dataframe = pd.DataFrame([[search_words,tweet.id, tweet.created_at, tweet.user.followers_count, tweet.user.verified, tweet.favorite_count, tweet.retweet_count, tweet.full_text.encode('utf-8')]], columns=['Search Words','Tweet Id', 'Tweet Date', 'Follower Count', 'Account Verified', 'Favorite Count', 'Retweets', 'Tweet Text'])
                tweet_dataset = tweet_dataset.append(appending_dataframe)
                counter+=1
                if counter >= 2:
                    break




print(tweet_dataset.info())
#tweet_dataset.to_excel('tweet_dataset.xlsx', index=False)
tweet_dataset_raw = tweet_dataset.copy()
tweet_dataset['Tweet Text'] = tweet_dataset['Tweet Text'].astype(str)
tweet_dataset['Tweet Text'] = tweet_dataset['Tweet Text'].apply(clean)

print(tweet_dataset.head(10))
print(tweet_dataset_raw.head(10))

#import os
#print(os.getcwd())
tweet_dataset.to_csv("tweet_dataset.csv")
tweet_dataset_raw.to_csv("tweet_dataset_raw.csv")



#import flair
#sentiment_model = flair.models.TextClassifier.load('en-sentiment')