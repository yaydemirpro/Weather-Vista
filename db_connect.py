from pymongo import MongoClient
from pymongo.errors import PyMongoError
from db_config import DB_USER, DB_PASSWORD, DB_CLUSTER

def get_db_connection():

    try:
        url = f'mongodb+srv://{DB_USER}:{DB_PASSWORD}@{DB_CLUSTER}.mongodb.net/'        
        client = MongoClient(url)
        db = client["citydb"]
        collection = db["citydb"]
        return collection       
    except PyMongoError as pe:        
        print(f'PyMongo error: {pe}')



