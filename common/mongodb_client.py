# sudo pip install pymongo

# need to start mongodb by:   sudo service mongod start/stop/restart    



from pymongo import MongoClient

MONGO_DB_HOST = 'localhost'
MONGO_DB_PORT = '27017'
DB_NAME = 'estate_db'

client = MongoClient('%s:%s' % (MONGO_DB_HOST,MONGO_DB_PORT))

def getDB(db=DB_NAME):
	db = client[db]
	return db