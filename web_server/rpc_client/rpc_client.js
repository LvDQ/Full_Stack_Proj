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

// Search property using address and city/state or zip code.
function searchByAddress(address, citystatezip, callback) {
    client.request('searchByAddress', [address, citystatezip], function(err, error, response) {
        if (err) throw err;
        console.log(response);
        callback(response);
    });
}

// Search properties using zip code.
function searchAreaByZip(zipcode, callback) {
    client.request('searchAreaByZip', [zipcode], function(err, error, response) {
        if (err) throw err;
        console.log(response);
        callback(response);
    });
}

// Search properties using city and state.
function searchAreaByCityState(city, state, callback) {
    client.request('searchAreaByCityState', [city, state], function(err, error, response) {
        if (err) throw err;
        console.log(response);
        callback(response);
    });
}

// Get property details by Zillow Property ID (zpid).
function getDetailsByZpid(zpid, callback) {
    client.request('getDetailsByZpid', [zpid], function(err, error, response) {
        if (err) throw err;
        console.log(response);
        callback(response);
    });
}


module.exports = {
    add : add,
    searchByAddress : searchByAddress,
    searchAreaByZip : searchAreaByZip,
    searchAreaByCityState : searchAreaByCityState,
    search_area: search_area
    getDetailsByZpid : getDetailsByZpid
};
