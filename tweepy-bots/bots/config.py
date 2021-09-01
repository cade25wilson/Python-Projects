# tweepy-bots/bots/config.py
import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("oFcs5YRLDQEzcXTRxN7E73l05")
    consumer_secret = os.getenv("5zfiRDbNVRklowIhK2eWGs19r5SQfPPQrzaUi46UKZ78cmlIn5")
    access_token = os.getenv("1430602494866907136-XkW3kDO8AO8qH5vnFwqTVh2gsn9yNm")
    access_token_secret = os.getenv("VFVeSl6kXMo6sqpCT3x6Mavz9JTEgNpoQHCGByz1UzTFh")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api


                          
    
