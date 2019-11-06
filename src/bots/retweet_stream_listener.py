import tweepy
import logging
from src.stream_listener import StreamListener
from src.twitter_api import get_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class RetweetStreamListener(StreamListener):
    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        # Ignore tweet if it's either mine or a reply
        if tweet.in_reply_to_status_id is not None or \
                tweet.user.id == self.me.id:
            return
        # Like
        if not tweet.favorited:
            try:
                # tweet.favorite()
                logger.info('Like')
            except Exception as e:
                logger.error(f"Error on like: {e}", exc_info=True)
        # Retweet
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                # tweet.retweet()
                logger.info('Retweet')
            except Exception as e:
                logger.error(f"Error on retweet: {e}", exc_info=True)


if __name__ == "__main__":
    api = get_api()
    stream_listener = RetweetStreamListener(api)
    stream_listener.stream(stream_listener, ["Python", "JavaScript", "OSS"])
