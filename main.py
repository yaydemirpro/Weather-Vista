import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QComboBox,QTableWidgetItem
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtCore import QSettings,QStringListModel, QTimer, QDateTime
from PyQt5.QtGui import QPixmap
from pymongo.errors import PyMongoError
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
from db_connect import get_db_connection, get_complete_url, get_forecast_url, get_complete_url


class WeatherVista(QMainWindow):
    def __init__(self):
        super(WeatherVista, self).__init__()        
        loadUi('weatherapp2.ui', self)
        self.setWindowTitle('Weather Vista')
        # Initialize settings
        self.settings = QSettings("WeatherVista", "country_city")

        
        # Load cities from database and store them in a variable
        self.cities_data = self.load_cities_from_database()
        self.cities = [] 

        # Connect the update_clock method to the QTimer timeout signal
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)  # Timer fires every second
      
        self.cities_list.currentIndexChanged.connect(lambda index: self.update_city_label(index, self.cities_list.currentText()))
        self.cities_list.currentIndexChanged.connect(self.update_weather_data)      
        self.cities_list.currentIndexChanged.connect(self.save_last_city_country)        

        # Fill countries into the county_list combobox element
        self.fill_countries_into_combobox() 
        self.update_city_label(0,self.cities_list.currentText())
        # Change cities according to country
        self.countries_list.currentIndexChanged.connect(lambda index: self.fill_cities_into_combobox(self.countries_list.itemText(index)))


        # Load last selected country and city
        last_country = self.settings.value("last_country", "")
        last_city = self.settings.value("last_city", "")
        self.country_index = 0  # Default value

        
        # Initialize selected country and city from comboboxes if they are not empty
        if self.countries_list.count() > 0:
            self.selected_country = self.countries_list.currentText()
        if self.cities_list.count() > 0:
            self.selected_city = self.cities_list.currentText()

        
        if last_country:
            self.country_index = self.countries_list.findText(last_country)
            if self.country_index != -1:
                self.countries_list.setCurrentIndex(self.country_index)

        if last_city:
            city_index = self.cities_list.findText(last_city)
            if city_index != -1:
                self.selected_city = last_city
                self.cities_list.setCurrentIndex(city_index)
        
   
        #search for cities from search QLineEdit
        self.search_city.setPlaceholderText("Find your city quickly 🔍")
        self.searched_cities = []
        # Create a QCompleter and set it for the search_city QLineEdit
        self.completer = QCompleter()
        self.search_city.setCompleter(self.completer)
        
        # Connect the textChanged signal to the search_city_with_QLineEdit method
        self.search_city.returnPressed.connect(self.search_city_with_QLineEdit)
        self.search_city.setPlaceholderText("")

        # Placeholder metnini animasyonlu hale getirmek için timer başlatma
        self.placeholder_timer = QTimer(self)
        self.placeholder_timer.timeout.connect(self.update_placeholder_text)
        self.placeholder_text = "Find your city quickly 🔍"
        self.placeholder_index = 0
        self.placeholder_timer.start(100)  # Her 100 milisaniyede bir timeout sinyali gönderir

    def update_placeholder_text(self):
        # Her çağrıda placeholder metnine bir sonraki harfi ekler
        if self.placeholder_index < len(self.placeholder_text):
            current_text = self.search_city.placeholderText()
            self.search_city.setPlaceholderText(current_text + self.placeholder_text[self.placeholder_index])
            self.placeholder_index += 1
        else:
            
            self.placeholder_timer.stop()  # Metnin tamamı yazıldıysa timer'ı durdur



    def update_clock(self):
        # Get the current date and time
        current_datetime = QDateTime.currentDateTime()
        # Update the date and time labels
        self.date_label.setText(current_datetime.toString("MMMM d, yyyy"))
        self.time_label.setText(current_datetime.toString("hh:mm:ss"))
        self.day_label.setText(current_datetime.toString("dddd"))
        
                
    def load_cities_from_database(self):
        cities_data = {}
        db_connection = get_db_connection()
        all_documents = db_connection.find()
        for document in all_documents:
            for country, cities in document.items():
                if country == "_id":
                    continue  # Skip the "_id" field
                cities_sorted_by_population = sorted(cities, key=lambda x: x.get("population", 0), reverse=True)
                cities_info = []
                for city_data in cities_sorted_by_population:
                    city_info = {
                        "city": city_data["city"],
                        "province": city_data.get("province", ""),
                        "population": city_data.get("population", 0)
                    }
                    cities_info.append(city_info)
                cities_data[country] = cities_info
        return cities_data

        

    def search_city_with_QLineEdit(self):
        text = self.search_city.text().lower()
        matched_cities = []
        for country, cities in self.cities_data.items():
            for city in cities:
                if text in city['city'].lower():  # Accessing the 'city' key from the dictionary
                    matched_cities.append((country, city))
        if matched_cities:
            selected_country, selected_city = matched_cities[0]
            self.update_country_and_city_comboboxes(selected_country, selected_city)
        self.search_city.clear()

    def update_country_and_city_comboboxes(self, selected_country, selected_city):
        # Ülke ve şehir bilgilerini güncelle ve combobox'ları ayarla
        country_index = self.countries_list.findText(selected_country)
        if country_index != -1:
            self.countries_list.setCurrentIndex(country_index)

        self.fill_cities_into_combobox(self.countries_list.currentText())

        city_index = self.cities_list.findText(selected_city["city"])
        if city_index != -1:
            self.cities_list.setCurrentIndex(city_index)


 
    def save_last_city_country(self):
        self.settings.setValue("last_country", self.countries_list.currentText())
        self.settings.setValue("last_city", self.cities_list.currentText())   
        
        
    def fill_countries_into_combobox(self):
        self.cities_list.currentIndexChanged.disconnect(self.save_last_city_country)           #********************************
        self.countries_list.clear()

        countries = [(index, country) for index, country in enumerate(self.cities_data.keys())]
        for index, country in countries:
            self.countries_list.addItem(country, index)

        # Otomatik olarak son seçili ülkeyi seç
        last_country = self.settings.value("last_country", "")
        if last_country:
            country_index = self.countries_list.findText(last_country)
            if country_index != -1:
                self.countries_list.setCurrentIndex(country_index)
                self.fill_cities_into_combobox(last_country)
        self.cities_list.currentIndexChanged.connect(self.save_last_city_country)           #********************************

    def fill_cities_into_combobox(self, selected_country):
        cities_in_country = self.cities_data.get(selected_country, [])
        self.cities_list.currentIndexChanged.disconnect(self.update_weather_data)           #********************************
        self.cities_list.clear()
        
        city_names = [city["city"] for city in cities_in_country]
        self.cities_list.addItems(city_names)
        self.cities_list.currentIndexChanged.connect(self.update_weather_data)              #********************************

        # Otomatik olarak son seçili şehri seç
        last_city = self.settings.value("last_city", "")
        if last_city in city_names:
            city_index = city_names.index(last_city)
            self.cities_list.setCurrentIndex(city_index)
              
    def update_city_label(self, index, selected_city_name):
        if selected_city_name:
            # Fetch city information from self.cities_data
            city_info = None
            for country, cities in self.cities_data.items():
                for city in cities:
                    if city["city"] == selected_city_name:
                        city_info = city
                        break
                if city_info:
                    break

            if city_info:
                # Update labels with data from the selected city
                self.city_name_label.setText(city_info["city"])
                self.province_label.setText(city_info["province"])
                self.population_label.setText(str(city_info["population"]))
                self.selected_country = self.countries_list.currentText()
            else:
                print(f"City data not found for {selected_city_name}")
        else:
            print("No city selected")

    def update_weather_data(self):
        selected_country = self.countries_list.currentText()
        selected_city = self.cities_list.currentText()
        
        # Fetch and update forecast and weather data for the selected city
        self.get_forecast_from_api(selected_country, selected_city)
        self.get_daily_forecast_from_api(selected_country, selected_city)
        self.get_weather_from_api(selected_country, selected_city)
            
            
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
            #print("today", today)
            
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
                
                #print(current_date)

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
                #print(three_hours)

                # Temperature is measured in Kelvin
                temperature = int(item['main']['temp'] - 273.15)
                # temperature = (int(temperature - 273.15))

                # Weather condition
                description = item['weather'][0]['description']

                # Prints the description as well as the temperature in Celsius and Fahrenheit


                # Additional weather information
                icon = item['weather'][0]['icon']
                
                forecast_data_to_db.append({ "date":day_date, "time": three_hours, "temperature": temperature, "icon": icon, "description": description})
            #show temparatures into foracastlabel
            self.forecast_temp_3hours.setText(str(forecast_data_to_db[0]['temperature']))
            self.forecast_temp_6hours.setText(str(forecast_data_to_db[1]['temperature']))
            self.forecast_temp_9hours.setText(str(forecast_data_to_db[2]['temperature']))
            self.forecast_temp_12hours.setText(str(forecast_data_to_db[3]['temperature']))
            #show icon into iconlabel
            icon_url = f"http://openweathermap.org/img/w/{forecast_data_to_db[0]['icon']}.png"
            icon_image = requests.get(icon_url)
            pixmap = QPixmap()
            pixmap.loadFromData(icon_image.content)
            self.forecast_icon_3hours.setPixmap(pixmap)
            
            icon_url = f"http://openweathermap.org/img/w/{forecast_data_to_db[1]['icon']}.png"
            icon_image = requests.get(icon_url)
            pixmap = QPixmap()
            pixmap.loadFromData(icon_image.content)
            self.forecast_icon_6hours.setPixmap(pixmap)
            
            icon_url = f"http://openweathermap.org/img/w/{forecast_data_to_db[2]['icon']}.png"
            icon_image = requests.get(icon_url)
            pixmap = QPixmap()
            pixmap.loadFromData(icon_image.content)
            self.forecast_icon_9hours.setPixmap(pixmap)
            
            icon_url = f"http://openweathermap.org/img/w/{forecast_data_to_db[2]['icon']}.png"
            icon_image = requests.get(icon_url)
            pixmap = QPixmap()
            pixmap.loadFromData(icon_image.content)
            self.forecast_icon_12hours.setPixmap(pixmap)            
            

        else:
            print(f"{city_name} Not Found")
            #print(forecast_data)
        
        
    def get_daily_forecast_from_api(self,country_name, city_name ):
        forecast_url = get_forecast_url(city_name)    
        apicall = requests.get(forecast_url)
        daily_forecast_data = apicall.json()
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
                    
                    

                    # Additional weather information
                    icon = item['weather'][0]['icon']
                    
                    


                    daily_forecast_data_db.append({"date" : day_date, "temperature": temperature, "description" : description,"icon": icon})
            # print(daily_forecast_data_db)
            
            self.forecast_temp_tomorrow.setText(str(daily_forecast_data_db[0]['temperature']))
            self.forecast_temp_after1.setText(str(daily_forecast_data_db[1]['temperature']))
            self.forecast_temp_after2.setText(str(daily_forecast_data_db[2]['temperature']))
            
            
            icon_url = f"http://openweathermap.org/img/w/{daily_forecast_data_db[0]['icon']}.png"
            icon_image = requests.get(icon_url)
            pixmap = QPixmap()
            pixmap.loadFromData(icon_image.content)
            self.forecast_icon_tomorrow.setPixmap(pixmap)
            
            icon_url = f"http://openweathermap.org/img/w/{daily_forecast_data_db[1]['icon']}.png"
            icon_image = requests.get(icon_url)
            pixmap = QPixmap()
            pixmap.loadFromData(icon_image.content)
            self.forecast_icon_after1.setPixmap(pixmap)
            
            icon_url = f"http://openweathermap.org/img/w/{daily_forecast_data_db[2]['icon']}.png"
            icon_image = requests.get(icon_url)
            pixmap = QPixmap()
            pixmap.loadFromData(icon_image.content)
            self.forecast_icon_after2.setPixmap(pixmap)

        else:
            print(f"{city_name} Not Found")


    def get_weather_from_api(self, country_name, city_name):
        complete_url = get_complete_url(city_name)    
        response = requests.get(complete_url)
        weather_data = response.json()
        try:
            if weather_data["cod"] != "200":
                # Extracting relevant information from the JSON response
                main_info = weather_data["main"]
                
                # Main information
                temperature = main_info["temp"]
                pressure = main_info["pressure"]
                humidity = main_info["humidity"]
                
                # Wind
                wind_info = weather_data.get("wind", {})  # Use .get() method to safely access wind_info
                wind_speed = wind_info.get("speed", "N/A")  # Use .get() method to safely access wind_speed

                # Description
                weather_info = weather_data["weather"]
                weather_description = weather_info[0]["description"]
                
                #icon
                weather_info = weather_data ["weather"]
                weather_icon = weather_info[0]["icon"]
                
                # Displaying the information
                self.temperature_label.setText(str(int(temperature))+"°c")
                self.pressure_label.setText(str(pressure)+"hPa")
                self.pressure_label_3.setText(str(humidity)+"%")
                self.wind_speed_label.setText(str(wind_speed)+"m/s")
                self.current_weather_description.setText((weather_description))
                
                icon_url = f"http://openweathermap.org/img/w/{weather_icon}.png"
                icon_image = requests.get(icon_url)
                pixmap = QPixmap()
                pixmap.loadFromData(icon_image.content)
                self.current_weather_icon.setPixmap(pixmap)

            else:
                print(f"{city_name} Not Found")

        except KeyError as e:
            error_message = f"An error occurred: {e}"
            QMessageBox.warning(self, "Error", error_message)



            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_vista = WeatherVista()
    weather_vista.show()
    sys.exit(app.exec_())
