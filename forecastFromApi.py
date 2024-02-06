import requests
from db_connect import get_db_connection, get_forecast_url
from pymongo.errors import PyMongoError

def get_forecast_from_api(country_name, city_name):
    
    forecast_url = get_forecast_url(city_name)    
    apicall = requests.get(forecast_url)
    forecast_data = apicall.json()

    if forecast_data["cod"] == "200":
        # Extracting relevant information from the JSON response
        main_info = forecast_data["list"][0]["main"]  # Assuming the first item in the list
        temperature = main_info["temp"]

        
        forecast_data_to_db = []
        today = forecast_data["list"][0]['dt_txt'].split(' ')[0]
        print("today", today)
        
        for x in range(0, 4):
            item = forecast_data["list"][x]
            # Time of the weather data received, partitioned into 3-hour blocks
            time = item['dt_txt']

            # Split the time into date and hour [2018-04-15 06:00:00]
            current_date, hour = time.split(' ')

            # Stores the current date and prints it once
            
            year, month, day = current_date.split('-')
            date = {'y': year, 'm': month, 'd': day}
            day_date = ('{m}/{d}/{y}'.format(**date))
            
            print(current_date)

            # Grabs the first 2 integers from our HH:MM:SS string to get the hours
            hour = int(hour[:2])

            # Sets the AM (ante meridiem) or PM (post meridiem) period
            if hour < 12:
                if hour == 0:
                    hour = 12
                meridiem = 'AM'
            else:
                if hour > 12:
                    hour -= 12
                meridiem = 'PM'

            # Prints the hours [HH:MM AM/PM]
            three_hours =('%i:00 %s' % (hour, meridiem))
            print(three_hours)

            # Temperature is measured in Kelvin
            temperature = int(item['main']['temp'] - 273.15)
            # temperature = (int(temperature - 273.15))

            # Weather condition
            description = item['weather'][0]['description']

            # Prints the description as well as the temperature in Celsius and Fahrenheit
            print('Weather condition: %s' % description)
            print(f'Celsius: {temperature} °C')

            # Additional weather information
            icon = item['weather'][0]['icon']
            print('Icon: {}'.format(icon))
            forecast_data_to_db.append({ "date":day_date, "time": three_hours, "temperature": temperature, "icon": icon, "description": description})
        
        insert_forecast_data(country_name, city_name, forecast_data_to_db)

    else:
        print(f"{city_name} Not Found")
        #print(forecast_data)
    
    get_daily_forecast_from_api(country_name, city_name, forecast_data)
    
####################################################################################################
def get_daily_forecast_from_api(country_name, city_name, daily_forecast_data):

    if daily_forecast_data["cod"] == "200":
        # Extracting relevant information from the JSON response
        main_info = daily_forecast_data["list"][0]["main"]  # Assuming the first item in the list
        temperature = main_info["temp"]

        daily_forecast_data_db = []
        today = daily_forecast_data["list"][0]['dt_txt'].split(' ')[0]

        for item in daily_forecast_data["list"]:
            # Time of the weather data received, partitioned into 3-hour blocks
            time = item['dt_txt']

            # Split the time into date and hour [2018-04-15 06:00:00]
            next_date, hour = time.split(' ')

            # Stores the current date and prints it once
            if today != next_date:
                today = next_date
                year, month, day = today.split('-')
                date = {'y': year, 'm': month, 'd': day}
                day_date = ('{m}/{d}/{y}'.format(**date))
                
                temperature = int(item['main']['temp']- 273.15)

                # Weather condition
                description = item['weather'][0]['description']
                print(day_date)

                # Prints the description as well as the temperature in Celsius and Fahrenheit
                print('Weather condition: %s' % description)
                print(f'Celsius: {temperature} °C')

                # Additional weather information
                icon = item['weather'][0]['icon']
                print('Icon: {}'.format(icon))
                


                daily_forecast_data_db.append({"date" : day_date, "temparature": temperature, "description" : description,"icon": icon})
                
        
        insert_daily_forecast_data(country_name, city_name, daily_forecast_data_db)

    else:
        print(f"{city_name} Not Found")
        
def insert_daily_forecast_data(country_name, city_name, daily_forecast_data):
    collection = get_db_connection()

    query = {f"{country_name}.city": city_name}
    update = {
        "$set": {
            f"{country_name}.$[elem].forecast": daily_forecast_data
        }
    }
    array_filters = [{"elem.city": city_name}]

    try:

        collection.update_one({}, update, array_filters=array_filters)
        print(f"Forecast data for {city_name}, {country_name} inserted successfully.")
    except PyMongoError as pe:
        print(f'Error inserting forecast data for {city_name}, {country_name}: {pe}')


def insert_forecast_data(country_name, city_name, forecast_data):
    collection = get_db_connection()

    query = {f"{country_name}.city": city_name}
    update = {
        "$set": {
            f"{country_name}.$[elem].forecast": forecast_data
        }
    }
    array_filters = [{"elem.city": city_name}]

    try:

        collection.update_one({}, update, array_filters=array_filters)
        print(f"Forecast data for {city_name}, {country_name} inserted successfully.")
    except PyMongoError as pe:
        print(f'Error inserting forecast data for {city_name}, {country_name}: {pe}')


