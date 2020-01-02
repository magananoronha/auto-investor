import os
import requests
from requests_oauthlib import OAuth1


def create_credentials():
    oauth_secret = os.environ['ALLY_OAUTH_SECRET']
    oauth_token = os.environ['ALLY_OAUTH_TOKEN']
    consumer_key = os.environ['ALLY_CONSUMER_KEY']
    consumer_secret = os.environ['ALLY_CONSUMER_SECRET']

    credentials = OAuth1(consumer_key,
                         client_secret=consumer_secret,
                         resource_owner_key=oauth_token,
                         resource_owner_secret=oauth_secret,
                         signature_type='auth_header'
                         )
    return credentials


def get_account_info():
    request_token_url = 'https://api.tradeking.com/v1/accounts.xml'
    creds = create_credentials()
    r = requests.get(url=request_token_url, auth=creds).content
    return r


def parse_account_info():
    pass
