import pyjsonrpc
# bson to string then string to json
import json
from bson.json_util import dumps

# import common package to parent directory
import os
import sys
"""
sys.path.append(os.path.join(os.path.dirname(__file__),'..','common'))

import mongodb_client

this is moved to operation.py
"""
import operations

sys.path.append(os.path.joinos.path.dirname((__file__),'..','data_fetcher'))

import zillow_api_client
import zillow_web_scraper_client


# Backend Server Code Below 

"""
# install pyjsonrpc: sudo pip install python-jsonrpc(not the similar package pyjsonrpc)

# We want to use rpc method to response requests, so we define new different actions(functions) in class `pyjsonrpc.rpcmethod`

# then if threre is any rpc request, we can return different response by using these new defined funcitons


"""

SERVER_HOST = 'localhost'
SERVER_PORT = 4040

TABLE_NAME = 'property'

class RequestHandler(pyjsonrpc.HttpRequestHandler):

    @pyjsonrpc.rpcmethod
    def add(self, a, b):
        """Test method"""
        return a + b


"""
    @pyjsonrpc.rpcmethod
    def searchArea(self, query):
    	res = []
    	if query.isdigit():
    		# TODO: search in DB
    		print "zipcode"
    		db = mongodb_client.getDB()
    		res = db[TABLE_NAME].find({'zipcode': query})
    		# bson to string to json, or throw err
    		res = json.loads(dumps(res))
    	else:
    		# eliminate ' ' in both side of the string by using .strip()
    		city = query.split(',')[0].strip()
    		state = query.split(',')[1].strip();
    		# TODO: search in DB
    	return res
"""
    """Search properties by zip code"""
    @pyjsonrpc.rpcmethod
    def searchAreaByZip(self, zipcode):
        print "searchAreaByZip() gets called with zipcode=[%s]" % str(zipcode)
        return operations.searchAreaByZip(zipcode)

    """Search properties by city and state"""
    @pyjsonrpc.rpcmethod
    def searchAreaByCityState(self, city, state):
        print "searchAreaByCityState() gets called with city=[%s] and state=[%s]" % (city, state)
        return operations.searchAreaByCityState(city, state)

    """Search properties"""
    @pyjsonrpc.rpcmethod
    def searchArea(self, text):
        print "search() gets called with text=[%s]" % text
        return operations.searchArea(text)

    """Retrieve details by zillow property ID (zpid)"""
    @pyjsonrpc.rpcmethod
    def getDetailsByZpid(self, zpid):
        print "getDetailsByZillowId() gets called with zpid=[%s]" % (zpid)
        return operations.getDetailsByZpid(zpid)

# Threading HTTP-Server
http_server = pyjsonrpc.ThreadingHttpServer(
    server_address = (SERVER_HOST, SERVER_PORT),
    RequestHandlerClass = RequestHandler
)

print "Starting HTTP server ..."
print "URL: http://%s:%d" % (SERVER_HOST,SERVER_PORT)


http_server.serve_forever()