import os
import sys
import time
import json

sys.path.append(os.path.join(os.path.dirname(__file__),'..','common'))

import mongodb_client
import zillow_web_scraper_client


from cloud_AMQP_client import Cloud_AMQP_Client

# RabbitMQ config

CLOUD_AMQP_URL = 'amqp://vvjncmjb:2titL4xyyEpg84GN_jTO_1QcFc9UMLWm@llama.rmq.cloudamqp.com/vvjncmjb'
QUEUE_NAME = 'Estate_Queue'

# Day time in seconds

SECONDS_ONE_DAY = 60 * 60 * 24
SECONDS_ONE_WEEK = SECONDS_ONE_DAY * 7


# mongodb config
PROPERTY_TABLE_NAME = 'estate_db'

FETCH_SIMILAR_PROPERTIES = False

client = Cloud_AMQP_Client(CLOUD_AMQP_URL,QUEUE_NAME)


def handle_message(msg):
	task = json.loads(msg)

	if(not isinstance(task,dict) or 
		not 'zpid' in task or 
		task['zpid'] is None):
		return

	zpid = task['zpid']

	#Scrape the zillow for details( decouple system )
	property_detail = zillow_web_scraper_client.get_property_by_zpid(zpid)

	# update doc in db
	db = mongodb_client.getDB()
	# if exists, then replace, if not exists, then insert
	db[PROPERTY_TABLE_NAME].replace_one({'zpid':zpid},property_detail, upsert = True)

	if FETCH_SIMILAR_PROPERTIES:
		# get its similar properties' zpid
		similar_zpids = zillow_web_scraper_client.get_similar_homes_for_sale_by_zpid(zpid)

		# generate tasks for similar zpids
		for zpid in similar_zpids:
			# avoid loop tasks
			db_homes = db[PROPERTY_TABLE_NAME].find_one({{'zpid':zpid}})
			if(db_homes is not None and time.time() - db_homes['last_update'] < SECONDS_ONE_WEEK ):
				continue
			client.sendDataFetcherTask({'zpid':zpid})



# Main thread loop
while True:
	# Fetch a message
	if client is not None:
		msg = client.getDataFetcherTask()
		if msg is not None:
			handle_message(msg)
		time.sleep(1)