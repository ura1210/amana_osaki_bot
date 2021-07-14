import tweepy
import os
import pandas as pd

def get_tenka():
    df = pd.read_csv('tenka.csv', header = None)
    title = pd.DataFrame({'ちゃん！？','ちゃーん☆','ちゃん！'})[0].sample().values[0]
    return f'{str(df[0].sample().values[0])}{title}'

def execute():
    CONSUMER_KEY = os.environ["consumer_key"]
    CONSUMER_SECRET = os.environ["consumer_secret"]
    ACCESS_TOKEN_KEY = os.environ["access_token_key"]
    ACCESS_TOKEN_SECRET = os.environ["access_token_secret"]

    tenka = get_tenka()
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.update_status(tenka)

def main():
    execute()

if __name__ == '__main__':
    main()