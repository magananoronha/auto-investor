import os
import requests
from requests_oauthlib import OAuth1

request_token_url = 'https://api.tradeking.com/v1/accounts.json'

oauth_secret = os.environ['ALLY_OAUTH_SECRET']
oauth_token = os.environ['ALLY_OAUTH_TOKEN']
consumer_key = os.environ['ALLY_CONSUMER_KEY']
consumer_secret = os.environ['ALLY_CONSUMER_SECRET']

tmp = OAuth1(consumer_key,
               client_secret=consumer_secret,
               resource_owner_key=oauth_token,
               resource_owner_secret=oauth_secret,
               signature_type='auth_header'
               )

r = requests.get(url=request_token_url, auth=tmp)
