import requests

def get_weather_from_api(city_name):
    api_key = "eb253155ca7e078cc3180d8356c7ce59"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    
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

    else:
        print(f"{city_name} Not Found")

# Example 
get_weather_from_api("Amsterdam")

