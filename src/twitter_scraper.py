import tweepy

import config


class TwitterScraper(object):
    api = None

    def __init__(self):
        auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET_KEY)
        auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth, wait_on_rate_limit=True,
                              wait_on_rate_limit_notify=True)

        try:
            self.api.verify_credentials()
            print("Authentication OK")
        except tweepy.TweepError as e:
            print("Error during authentication: {}".format(e))

    def query_tweets(
            self,
            query: str,
            lang: str = "en",
            count: int = 1,
            result_type: str = "mixed",
            max_date: str = "",
            geocode: str = "",
    ):
        """
        :param query: Can include @, #, etc.
        :param lang: ISO 639-1 code (https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)
        :param count: Number of tweets to retrieve
        :param result_type: Accepts 'mixed' or 'recent' or 'popular'
        :param max_date: Date as 'YYYY-MM-DD'. 7 day limit - returns tweets before this date
        :param geocode: 'latitude' (float) 'longitude' (float) 'radius' (mi/km)
        :return:
        """

        count = min(count, 1)

        tweets = self.api.search(
            q=query,
            lang=lang,
            rpp=count,
            until=max_date,
            result_type=result_type,
            geocode=geocode
        )
        return tweets

    def stream(self, track_query: list, languages: list = None):
        if not languages:
            languages = ["en"]
        tweet_listener = StreamListener(self.api)
        stream = tweepy.Stream(self.api.auth, tweet_listener)
        stream.filter(track=track_query, languages=languages)

    def get_worldwide_trends(self):
        trends_result = self.api.trends_place(1)
        for trend in trends_result[0]["trends"]:
            print(trend["name"])

    def get_user(self, user_name: str):
        """
        User details:
        - name
        - description
        - location
        :param user_name:
        :return: user object
        """
        user = self.api.get_user(user_name)
        return user

    def post_tweet(self, message: str) -> None:
        self.api.update_status(message)

    def follow_user(self, user_name: str) -> None:
        self.api.create_friendship(user_name)

    def like_tweet(self, tweet_id: str) -> None:
        self.api.create_favorite(tweet_id)

    def get_home_timeline(self, count: int = 20):
        """
        :return: Last n entries of the owning account's timeline (n = count)
        """
        timeline = self.api.home_timeline(count=count)
        return timeline

    def get_user_timeline(self, user_name: str, count: int = 20):
        timeline = self.api.user_timeline(user_name, count=count)
        return timeline

    def update_profile_description(self, description: str) -> None:
        self.api.update_profile(description=description)


class StreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")
