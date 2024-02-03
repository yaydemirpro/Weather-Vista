import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QComboBox,QTableWidgetItem
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
from db_connect import get_db_connection, get_complete_url



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
        self.tableWidget.setColumnCount(4)
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



    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_vista = WeatherVista()
    weather_vista.show()
    sys.exit(app.exec_())
