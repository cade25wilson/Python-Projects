import tweepy
auth = tweepy.OAuthHandler("N91DlurhYfswAfvqff6z0llf9", "IqdqFjYTHHJdnhsbR3Bj9HdVPLWxMIeGbQMFHJCg65opmqX10d")
auth.set_access_token("1430602494866907136-Tqtdw8bHROhPz4xIPhsatiq4Jpb6Qv", "s7xiMKDRhOIbgK6lX7rAiBsQt9RR60maqVD3N3SitS1us")
api = tweepy.API(auth)
try:
	api.verify_credentials()
	print("Authentication OK")
except:
	print("Error during authentication")

timeline = api.home_timeline()
for tweet in timeline:
        print(f"{tweet.user.name} said {tweet.text}")

def custom_tweet():
        tweet = input("what would you like to tweet about?")
        api.update_status(tweet)
        print(timeline)
