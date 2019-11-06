import logging
import tweepy
import config

logger = logging.getLogger()


def get_api():
    auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET_KEY)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    api = tweepy.API(
        auth,
        wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True
    )
    
    try:
        api.verify_credentials()
    except tweepy.TweepError as e:
        logger.error('Error creating API', exc_info=True)
        raise e
    logger.info('API Created')
    return api


def query_tweets(
        api: tweepy.API,
        query: str,
        lang: str = "en",
        count: int = 1,
        result_type: str = "mixed",
        max_date: str = "",
        geocode: str = "",
):
    """
    :param api: Twitter API object
    :param query: Can include @, #, etc.
    :param lang: ISO 639-1 code (https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)
    :param count: Number of tweets to retrieve
    :param result_type: Accepts 'mixed' or 'recent' or 'popular'
    :param max_date: Date as 'YYYY-MM-DD'. 7 day limit - returns tweets before this date
    :param geocode: 'latitude' (float) 'longitude' (float) 'radius' (mi/km)
    :return:
    """
    
    count = min(count, 1)
    
    response = api.search(
        q=query,
        lang=lang,
        rpp=count,
        until=max_date,
        result_type=result_type,
        geocode=geocode
    )
    return response


if __name__ == '__main__':
    test_api = get_api()
    
    # Get user data
    user = test_api.get_user("timrodz")
    
    print("User details:")
    print(user.name)
    print(user.description)
    print(user.location)
    
    print("Last 20 Followers:")
    for follower in user.followers():
        print(follower.name)
    
    # Get user timeline
    tweets = test_api.user_timeline("timrodz", count=1)
    for tweet in tweets:
        print(f"Liking tweet {tweet.text} of {tweet.author.name}")
    
    # # Query random data
    tweets = query_tweets(
        test_api,
        "#gamedev",
        lang="es",
        count=10,
        result_type="mixed"
    )
    for tweet in tweets:
        print(f"TWEET: {tweet.user.name}//{tweet.text}")
