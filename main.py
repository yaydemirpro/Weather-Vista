import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox


class WeatherVista(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Weather Vista')

              # Fill cities
        self.fill_cities('Belgium')  # Başlangıçta Belgika şehirlerini göster

        # Change cities according to country
        self.country_combobox.currentIndexChanged.connect(self.on_country_changed)
        
        
        
    def fill_cities(self, country):
        
        cities = self.get_cities_from_database(country)
        self.city_combobox.clear()
        self.city_combobox.addItems(cities)
        
    def get_cities_from_database(self, country):
                  

        return []

    def on_country_changed(self):
        selected_country = self.country_combobox.currentText()
        self.fill_cities(selected_country)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    WeatherVista = WeatherVista()
    WeatherVista.show()
    sys.exit(app.exec_())