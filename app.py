from dotenv import load_dotenv
from post_anchor import anchor_connect
from search_tweet import twitter_connect



if __name__ == '__main__':
    load_dotenv()
    anchor_connect()
    twitter_connect()