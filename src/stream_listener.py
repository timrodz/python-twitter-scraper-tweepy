import logging
import tweepy
from src.twitter_api import get_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class StreamListener(tweepy.StreamListener):
    def __init__(self, api: tweepy.API):
        self.api = api
        self.me = api.me()
    
    def on_status(self, tweet):
        logger.info(f"{tweet.user.name}:{tweet.text}")
    
    def on_error(self, status):
        logger.error(f"Error detected: {status}", exc_info=True)
    
    def stream(self, listener: tweepy.StreamListener, track_query: list,
               languages: list = None):
        if not languages:
            languages = ["en"]
        stream = tweepy.Stream(self.api.auth, listener)
        stream.filter(track=track_query, languages=languages)


if __name__ == '__main__':
    test_api = get_api()
    stream_listener = StreamListener(test_api)
    stream_listener.stream(["Python", "Tweepy"])
