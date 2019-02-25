// need to install jayson by sudo npm install --save jayson


var jayson = require('jayson');

SERVER_HOST = 'localhost'
SERVER_PORT = 4040

//create a client connected to backend server

var client = jayson.client.http({
	hostname: SERVER_HOST,
	port: SERVER_PORT
})


//Test RPC method add() from ./backend/server.py

function add(a,b,callback){
	//first 'add' is the backend python function name('./backend/server.py'), second one is a list which contains a and b
	//first err is error such as backend error return, second error is the exception of rpc method
	client.request('add',[a,b],function(err,error,response){
		if(err) throw err;
		console.log(response);
		callback(response);
	})
}


//search area method by using zip code
function search_area(query,callback){
	client.request('searchArea',[query], function(err,error,response){
		if(err) throw err;
		console.log(response);
		callback(response);
	})
}


module.exports = {
	add: add,
	search_area: search_area
}