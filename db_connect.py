from pymongo import MongoClient
from pymongo.errors import PyMongoError
from db_config import DB_USER, DB_PASSWORD, DB_CLUSTER, base_url, api_key

def get_db_connection():

    try:
        url = f'mongodb+srv://{DB_USER}:{DB_PASSWORD}@{DB_CLUSTER}.mongodb.net/'        
        client = MongoClient(url)
        db = client["citydb"]
        collection = db["citydb"]
        return collection       
    except PyMongoError as pe:        
        print(f'PyMongo error: {pe}')

def get_complete_url(city_name):
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    return complete_url

