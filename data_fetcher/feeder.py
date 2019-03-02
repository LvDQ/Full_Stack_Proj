import os
import sys
import time

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client
import zillow_api_client
import zillow_web_scraper_client

from cloud_AMQP_client import Cloud_AMQP_Client

# Automatically feed zpids into queue
### REPLACE CLOUD_AMQP_URL WITH YOUR OWN ###
CLOUD_AMQP_URL = '''amqp://vvjncmjb:2titL4xyyEpg84GN_jTO_1QcFc9UMLWm@llama.rmq.cloudamqp.com/vvjncmjb'''
DATA_FETCHER_QUEUE_NAME = 'Estate_Queue'
ZIPCODE_FILE = 'zipcode_list.txt'

WAITING_TIME = 3

cloudAMQP_client = Cloud_AMQP_Client(CLOUD_AMQP_URL, DATA_FETCHER_QUEUE_NAME)

zipcode_list = []

with open(ZIPCODE_FILE, 'r') as zipcode_file:
    for zipcode in zipcode_file:
        zipcode_list.append(str(zipcode))

for zipcode in zipcode_list:
    zpids = zillow_web_scraper_client.search_zillow_by_zip(zipcode)
    time.sleep(WAITING_TIME)

    for zpid in zpids:
        cloudAMQP_client.sendDataFetcherTask({'zpid': zpid})

