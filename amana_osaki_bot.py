import twitter
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
    api = twitter.Api(consumer_key=CONSUMER_KEY,
                    consumer_secret=CONSUMER_SECRET, 
                    access_token_key=ACCESS_TOKEN_KEY,
                    access_token_secret=ACCESS_TOKEN_SECRET)
    api.PostUpdates(get_tenka())

def main():
    execute()

if __name__ == '__main__':
    main()