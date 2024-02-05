import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QComboBox,QTableWidgetItem
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtCore import QSettings,QStringListModel
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
