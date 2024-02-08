import requests
from db_connect import get_db_connection, get_complete_url
from pymongo.errors import PyMongoError


def get_weather_from_api(country_name, city_name):
    
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
        
        #icon
        weather_info = weather_data ["weather"]
        weather_icon = weather_info[0]["icon"]
        
        

        # Displaying the information
        print(f"Weather in {city_name}:")
        print(f"Temperature (in Celsius) = {int(temperature)} °C")
        print(f"Atmospheric pressure (in hPa) = {pressure} hPa")
        print(f"Humidity (in percentage) = {humidity}%")
        print(f"Wind Speed = {wind_speed} m/s")
        print(f"Weather description = {weather_description}")
        print(f"Icon:{weather_icon}")


        #insert_weather_data(country_name, city_name, { "temperature": temperature, "pressure": pressure, "humidity": humidity, "wind_speed": wind_speed, "weather_description": weather_description,"Icon": weather_icon})

    else:
        print(f"{city_name} Not Found")


# def insert_weather_data(country_name, city_name, weather_data):
#     collection = get_db_connection()

#     update = {
#         "$set": {
#             f"{country_name}.$[elem].forecast": weather_data
#         }
#     }
#     array_filters = [{"elem.city": city_name}]

#     try:
#         collection.update_one({}, update, array_filters=array_filters)
#     except PyMongoError as pe:
#         print(f'Error inserting forecast data for {city_name}, {country_name}: {pe}')

# # Example 
get_weather_from_api("Netherlands","Groningen")

