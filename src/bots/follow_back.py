import logging
import time
import tweepy
from src.twitter_api import get_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class FollowBackBot(object):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
    
    def check_for_new_followers(self):
        logger.info("Retrieving and following followers")
        for follower in tweepy.Cursor(self.api.followers).items():
            if not follower.following:
                logger.info(f"Following {follower.name}")
                follower.follow()


if __name__ == "__main__":
    test_api = get_api()
    follow_back = FollowBackBot(test_api)
    while True:
        follow_back.check_for_new_followers()
        logger.info("Waiting...")
        time.sleep(60)
