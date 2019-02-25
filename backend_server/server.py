import pyjsonrpc
import json


# Backend Server Code Below 

"""
# install pyjsonrpc: sudo pip install python-jsonrpc(not the similar package pyjsonrpc)

# We want to use rpc method to response requests, so we define new different actions(functions) in class `pyjsonrpc.rpcmethod`

# then if threre is any rpc request, we can return different response by using these new defined funcitons


"""

SERVER_HOST = 'localhost'
SERVER_PORT = 4040



class RequestHandler(pyjsonrpc.HttpRequestHandler):

    @pyjsonrpc.rpcmethod
    def add(self, a, b):
        """Test method"""
        return a + b



    @pyjsonrpc.rpcmethod
    def searchArea(self, query):
    	if query.isdigit():
    		# TODO: search in DB
    		print "zipcode"
    	else:
    		# eliminate ' ' in both side of the string by using .strip()
    		city = query.split(',')[0].strip()
    		state = query.split(',')[1].strip();
    		# TODO: search in DB
    	return ["House1","House_2"]


# Threading HTTP-Server
http_server = pyjsonrpc.ThreadingHttpServer(
    server_address = (SERVER_HOST, SERVER_PORT),
    RequestHandlerClass = RequestHandler
)

print "Starting HTTP server ..."
print "URL: http://%s:%d" % (SERVER_HOST,SERVER_PORT)


http_server.serve_forever()