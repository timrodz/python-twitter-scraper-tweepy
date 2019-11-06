from src.twitter_scraper import TwitterScraper

if __name__ == "__main__":
    scraper = TwitterScraper()

    # Get user data
    user = scraper.get_user("timrodz")

    print("User details:")
    print(user.name)
    print(user.description)
    print(user.location)

    print("Last 20 Followers:")
    for follower in user.followers():
        print(follower.name)

    # Get user timeline
    tweets = scraper.get_user_timeline("timrodz", 1)
    for tweet in tweets:
        print(f"Liking tweet {tweet.text} of {tweet.author.name}")

    # # Query random data
    tweets = scraper.query_tweets(
        "#gamedev", lang="es", count=10, result_type="mixed")
    for tweet in tweets:
        print(f"TWEET: {tweet.user.name}//{tweet.text}")

    # Stream
    scraper.stream(["Python", "Django", "Tweepy"])
