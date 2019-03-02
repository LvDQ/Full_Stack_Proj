from cloud_AMQP_client import Cloud_AMQP_Client

# copy from RabitAMQP official web inistance
CLOUD_AMQP_URL = 'amqp://vvjncmjb:2titL4xyyEpg84GN_jTO_1QcFc9UMLWm@llama.rmq.cloudamqp.com/vvjncmjb'
QUEUE_NAME = 'Estate_Queue'

# initialize a client
client = Cloud_AMQP_Client(CLOUD_AMQP_URL,QUEUE_NAME)

# Send a Message

#client.sendDataFetcherTask({'name' : 'This is a test message.'})


# Receive a Message

client.getDataFetcherTask()

