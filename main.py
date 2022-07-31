from dotenv import load_dotenv
from search_tweet import twitter_connect

if __name__ == '__main__':
    load_dotenv()
    twitter_connect()
