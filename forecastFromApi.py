import requests
from db_connect import get_db_connection, get_forecast_url
from pymongo.errors import PyMongoError

def get_forecast_from_api(city_name):
    
    forecast_url = get_forecast_url(city_name)    
    apicall = requests.get(forecast_url)
    forecast_data = apicall.json()

    if forecast_data["cod"] == "200":
        # Extracting relevant information from the JSON response
        main_info = forecast_data["list"][0]["main"]  # Assuming the first item in the list
        temperature = main_info["temp"]

        current_date = ''

        for item in forecast_data["list"]:
            # Time of the weather data received, partitioned into 3-hour blocks
            time = item['dt_txt']

            # Split the time into date and hour [2018-04-15 06:00:00]
            next_date, hour = time.split(' ')

            # Stores the current date and prints it once
            if current_date != next_date:
                current_date = next_date
                year, month, day = current_date.split('-')
                date = {'y': year, 'm': month, 'd': day}
                day_date = ('\n{m}/{d}/{y}'.format(**date))
                
                print(day_date)

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
            three_hours =('\n%i:00 %s' % (hour, meridiem))
            print(three_hours)

            # Temperature is measured in Kelvin
            temperature = item['main']['temp']

            # Weather condition
            description = item['weather'][0]['description']

            # Prints the description as well as the temperature in Celsius and Fahrenheit
            print('Weather condition: %s' % description)
            print('Celsius: {} °C'.format(int(temperature - 273.15)))

            # Additional weather information
            icon = item['weather'][0]['icon']
            print('Icon: {}'.format(icon))
            
            # insert_forecast_data(city_name, { "date":day_date, "time": three_hours, "temperature": temperature, "icon": icon, "description": description})

    else:
        print(f"{city_name} Not Found")
        #print(forecast_data)


# def insert_forecast_data(city_name, forecast_data):
#         try:
#             collection = get_db_connection()      
#             existing_city = collection.find_one({"city_name": city_name})
                
#             if existing_city:                
#                 collection.update_one({"city_name": city_name}, {"$set": {"forecast_data": forecast_data}})
#                 print(f"Weather data for {city_name} updated in the database.")
#             else:                
#                 collection.insert_one({"city_name": city_name, "forecast_data": forecast_data})
#                 print(f"Forecast data for {city_name} inserted into the database.")

#         except PyMongoError as pe:
#             print(f'PyMongo error: {pe}')





get_forecast_from_api("Amsterdam")
