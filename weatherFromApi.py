import requests
from db_connect import get_db_connection, get_complete_url
from pymongo.errors import PyMongoError


def get_weather_from_api(city_name):
    
    complete_url = get_complete_url(city_name)    
    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data["cod"] != "404":
        # Extracting relevant information from the JSON response
        main_info = weather_data["main"]
        
        # Main information
        temperature = main_info["temp"]
        pressure = main_info["pressure"]
        humidity = main_info["humidity"]
        
        # Wind
        wind_info = weather_data["wind"]
        wind_speed = wind_info["speed"]

        # Description
        weather_info = weather_data["weather"]
        weather_description = weather_info[0]["description"]

        # Displaying the information
        print(f"Weather in {city_name}:")
        print(f"Temperature (in Celsius) = {int(temperature)} °C")
        print(f"Atmospheric pressure (in hPa) = {pressure} hPa")
        print(f"Humidity (in percentage) = {humidity}%")
        print(f"Wind Speed = {wind_speed} m/s")
        print(f"Weather description = {weather_description}")

        insert_weather_data(city_name, { "temperature": temperature, "pressure": pressure, "humidity": humidity, "wind_speed": wind_speed, "weather_description": weather_description})

    else:
        print(f"{city_name} Not Found")


    def insert_weather_data(city_name, weather_data):
        try:
            collection = get_db_connection()      
            existing_city = collection.find_one({"city_name": city_name})
            
            if existing_city:                
                collection.update_one({"city_name": city_name}, {"$set": {"weather_data": weather_data}})
                print(f"Weather data for {city_name} updated in the database.")
            else:                
                collection.insert_one({"city_name": city_name, "weather_data": weather_data})
                print(f"Weather data for {city_name} inserted into the database.")

        except PyMongoError as pe:
            print(f'PyMongo error: {pe}')

# Example 
get_weather_from_api("Amsterdam")