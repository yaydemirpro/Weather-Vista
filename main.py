import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QComboBox,QTableWidgetItem
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtCore import QSettings,QStringListModel
from PyQt5.QtGui import QPixmap
from pymongo.errors import PyMongoError
from PyQt5.uic import loadUi
from db_connect import get_db_connection, get_complete_url, get_forecast_url, get_complete_url



class WeatherVista(QMainWindow):
    def __init__(self):
        super(WeatherVista, self).__init__()        
        loadUi('weatherapp.ui', self)
        self.setWindowTitle('Weather Vista')
        
        # Fill countries into the county_list combobox element
        self.fill_countries_into_combobox() 

        
        # Initialize settings
        self.settings = QSettings("WeatherVista", "country_city")

        # Load last selected country and city
        last_country = self.settings.value("last_country", "")
        last_city = self.settings.value("last_city", "")
        self.country_index = 0  # Default value

        if last_country:
            self.country_index = self.countries_list.findText(last_country)
            if self.country_index != -1:
                self.countries_list.setCurrentIndex(self.country_index)

        if last_city:
            city_index = self.cities_list.findText(last_city)
            if city_index != -1:
                self.cities_list.setCurrentIndex(city_index)
        
        self.fill_cities_into_combobox(self.country_index)
        # Change cities according to country
        self.countries_list.currentIndexChanged.connect(self.fill_cities_into_combobox)
        self.cities_list.currentIndexChanged.connect(self.update_city_label)
        
        #search for cities from search QLineEdit
        self.search_city.setPlaceholderText("Search City")
        self.searched_cities = []
        self.selected_country = ""
        self.selected_city = ""
        # Create a QCompleter and set it for the search_city QLineEdit
        self.completer = QCompleter()
        self.search_city.setCompleter(self.completer)

        # Connect the completer to a custom filtering function
        self.completer.activated.connect(self.handle_completer_activated)
        
        # Connect the textChanged signal to the search_city_with_QLineEdit method
        self.search_city.textChanged.connect(self.search_city_with_QLineEdit)
        
        # Connect the cellClicked signal to the handle_cell_clicked method
        self.tableWidget.cellClicked.connect(self.handle_cell_clicked)
        
    def handle_cell_clicked(self, row, column):
        # Handle the cell click event
        if column == 0:  # Assuming the city name is in the first column
            selected_city_name = self.tableWidget.item(row, column).text()
            # Assuming that the city_name_label should be updated
            self.city_name_label.setText(selected_city_name)

            # Find the city data for the selected city
            selected_city_data = next((city_data for city_data in self.cities if city_data["city"] == selected_city_name), None)

            if selected_city_data:
                # Update labels with data from the selected city
                self.city_name_label.setText(selected_city_data["city"])
                self.province_label.setText(selected_city_data["province"])
                self.population_label.setText(str(selected_city_data["population"]))

                # Update the cities_list combobox
                selected_country = selected_city_data["country"]
                self.update_country_and_city_comboboxes(selected_country, selected_city_name)
        
    def search_city_with_QLineEdit(self, text):
        # Şehir araması yapılır
        self.searched_cities = []

        db_connection = get_db_connection()

        for document in db_connection.find():
            if "_id" not in document:
                continue  # Skip documents without "_id" field

            for country, cities in document.items():
                if country == "_id":
                    continue  # Skip the "_id" field

                for city_data in cities:
                    if text.lower() in city_data["city"].lower():
                        self.searched_cities.append({"country": country, "city": city_data["city"]})


        # Update the completer model with matching city names
        completer_model = QStringListModel([city["city"] for city in self.searched_cities])
        self.completer.setModel(completer_model)
        # If there is a match, update the comboboxes
        if self.searched_cities:
            selected_country = self.searched_cities[0]["country"]
            selected_city = self.searched_cities[0]["city"]
            self.update_country_and_city_comboboxes(selected_country, selected_city)


    def handle_completer_activated(self, index):
        # Handle the completion item selection if needed
        selected_city_name = self.completer.currentCompletion()


    def update_country_and_city_comboboxes(self, selected_country, selected_city):
        # Ülke ve şehir bilgilerini güncelle ve combobox'ları ayarla
        country_index = self.countries_list.findText(selected_country)
        if country_index != -1:
            self.countries_list.setCurrentIndex(country_index)

        self.fill_cities_into_combobox(country_index)

        city_index = self.cities_list.findText(selected_city)
        if city_index != -1:
            self.cities_list.setCurrentIndex(city_index)

            
                    
    def fill_countries_into_combobox(self):
        db_connection = get_db_connection()    
        all_documents = db_connection.find()
        
        countries = [country for document in all_documents for country in document.keys() if country != '_id']
        self.countries_list.clear()
        self.countries_list.addItems(countries)


    def fill_cities_into_combobox(self, index):
        selected_country = self.countries_list.itemText(index)
        db_connection = get_db_connection() 
        document = db_connection.find_one({selected_country: {"$exists": True}})     
        if document:
            self.cities = sorted(document[selected_country], key=lambda x: x["population"], reverse=True)
            self.cities_list.clear()
            self.cities_list.addItems([entry["city"] for entry in self.cities])
        else:
            print("Selected country has no cities")
        
        self.populate_table_widget(self.cities)


    def populate_table_widget(self, cities):
        self.tableWidget.setRowCount(len(cities))
        self.tableWidget.setColumnCount(3)
        headers = ["City Name", "Province", "Population"]
        self.tableWidget.setHorizontalHeaderLabels(headers)

        for row, city_data in enumerate(cities):
            if isinstance(city_data, dict):
                city_name = city_data.get("city", "")
                province = city_data.get("province", "")
                population = str(city_data.get("population", ""))

                self.tableWidget.setItem(row, 0, QTableWidgetItem(city_name))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(province))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(population))
            
    def update_city_label(self, index):
        selected_city = self.cities_list.itemText(index)

        # Find the city data for the selected city
        selected_city_data = next((city_data for city_data in self.cities if city_data["city"] == selected_city), None)

        if selected_city_data:
            # Update labels with data from the selected city
            self.city_name_label.setText(selected_city_data["city"])
            self.province_label.setText(selected_city_data["province"])
            self.population_label.setText(str(selected_city_data["population"]))
        else:
            print(f"Data not found for {selected_city}")

    def get_forecast_from_api(self, country_name, city_name):
        
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
            
            self.insert_forecast_data(country_name, city_name, forecast_data_to_db)

        else:
            print(f"{city_name} Not Found")
            #print(forecast_data)
        
        self.get_daily_forecast_from_api(country_name, city_name, forecast_data)
        
    def get_daily_forecast_from_api(self, country_name, city_name, daily_forecast_data):

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
                    
            
            self.insert_daily_forecast_data(country_name, city_name, daily_forecast_data_db)

        else:
            print(f"{city_name} Not Found")
            
    def insert_daily_forecast_data(self, country_name, city_name, daily_forecast_data):
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

        except PyMongoError as pe:
            print(f'Error inserting daily forecast data for {city_name}, {country_name}: {pe}')


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

        except PyMongoError as pe:
            print(f'Error inserting forecast data for {city_name}, {country_name}: {pe}')

    def get_weather_from_api(self, country_name, city_name):
        
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


            self.insert_weather_data(country_name, city_name, { "temperature": temperature, "pressure": pressure, "humidity": humidity, "wind_speed": wind_speed, "weather_description": weather_description,"Icon": weather_icon})

        else:
            print(f"{city_name} Not Found")


    def insert_weather_data(self, country_name, city_name, weather_data):
        collection = get_db_connection()

        query = {f"{country_name}.city": city_name}
        update = {
            "$set": {
                f"{country_name}.$[elem].forecast": weather_data
            }
        }
        array_filters = [{"elem.city": city_name}]

        try:
            collection.update_one({}, update, array_filters=array_filters)

        except PyMongoError as pe:
            print(f'Error inserting weather data for {city_name}, {country_name}: {pe}')
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_vista = WeatherVista()
    weather_vista.show()
    sys.exit(app.exec_())
