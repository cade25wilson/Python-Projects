import tweepy
auth = tweepy.OAuthHandler("(api key)", "(api secret key)")
auth.set_access_token("(access token)", "(secret access token)")
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
