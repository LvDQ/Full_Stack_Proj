var client = require('./rpc_client');

client.add(1,2,function(response){
	console.log("1 + 2 = " + response);
});

client.search_area('11220',function(response){
	console.log('Searched 11220 Houses : '+ response )
})