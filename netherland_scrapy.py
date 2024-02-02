from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import json
from db_config import DB_USER, DB_PASSWORD, DB_CLUSTER
from db_connect import get_db_connection

with open('netherland.json', 'r') as file:
    json_data = json.load(file)

formatted_data = {}
for entry in json_data:
    try:
        name = entry["name"]
        province = entry["province"]
        population = entry["population"].replace(",", "")  
        flag = entry.get("flag", "")  
    except KeyError as e:
        print(f"Error: Key not found in entry: {entry}")
        continue
    entry["country"] = "Netherlands"


    city_list = formatted_data.get("Netherlands", [])
    city_list.append({
        "country" : "Netherlands",
        "province": province,
        "flag": flag,
        "city": name,        
        "population": int(population)
        
    })
    formatted_data["Netherlands"] = city_list


db_connection = get_db_connection()


for country, city_list in formatted_data.items():
    existing_data = db_connection.find_one({country: {'$exists': True}})
    
    if existing_data:
        print(f"Data for {country} already exists in the database.")
    else:
        try:
            db_connection.insert_one({country: city_list})
        except DuplicateKeyError:
            print(f"Data for {country} already exists in the database.")
