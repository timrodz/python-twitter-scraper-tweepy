# Twitter Scraper using Tweepy

Python based scraper that uses the [Tweepy](https://www.tweepy.org/) python library. 

## How-to

The `TwitterScraper` class contains the basic Twitter interactions such as Likes, Follows, Retweets, etc. You can also set up a new tweet listener through the `StreamListener` class.

**IMPORTANT**: You will need to apply for a Twitter Developer account & acquire API Authentication credentials. Read more in this tutorial by [Real Python](https://realpython.com/twitter-bot-python-tweepy/#creating-twitter-api-authentication-credentials).

Once you authenticate your credentials, store them inside a `config.py` file. Make sure they're named like so:
- `API_KEY`
- `API_SECRET_KEY`
- `ACCESS_TOKEN`
- `ACCESS_TOKEN_SECRET`

If you wish to store these credentials somewhere else, make sure to change the imports accordingly in lines 3, 10 & 11 of `twitter_scraper.py`.
