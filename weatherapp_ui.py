# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weatherapp.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 900)
        MainWindow.setMinimumSize(QSize(750, 900))
        MainWindow.setMaximumSize(QSize(750, 900))
        MainWindow.setStyleSheet(u"background-color: rgb(154, 192, 214);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 761, 51))
        font = QFont()
        font.setFamilies([u"Papyrus"])
        font.setPointSize(39)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(84, 91, 134);\n"
"color: rgb(154, 192, 214);")
        self.label.setAlignment(Qt.AlignCenter)
        self.countries_list = QComboBox(self.centralwidget)
        self.countries_list.setObjectName(u"countries_list")
        self.countries_list.setGeometry(QRect(0, 60, 371, 38))
        font1 = QFont()
        font1.setFamilies([u"Sitka Banner"])
        font1.setPointSize(14)
        self.countries_list.setFont(font1)
        self.countries_list.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid rgb(103, 103, 103);\n"
"border-radius: 10px;\n"
"color: rgb(272, 191, 130);")
        self.search_city = QLineEdit(self.centralwidget)
        self.search_city.setObjectName(u"search_city")
        self.search_city.setGeometry(QRect(0, 110, 741, 41))
        font2 = QFont()
        font2.setFamilies([u"Papyrus"])
        font2.setPointSize(14)
        self.search_city.setFont(font2)
        self.search_city.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid rgb(272, 192, 125);\n"
"border-radius: 10px;")
        self.current_weather_icon = QLabel(self.centralwidget)
        self.current_weather_icon.setObjectName(u"current_weather_icon")
        self.current_weather_icon.setGeometry(QRect(80, 270, 170, 170))
        self.current_weather_icon.setMinimumSize(QSize(170, 170))
        self.current_weather_icon.setMaximumSize(QSize(170, 170))
        font3 = QFont()
        font3.setPointSize(7)
        self.current_weather_icon.setFont(font3)
        self.current_weather_icon.setStyleSheet(u"\n"
"background: none;")
        self.current_weather_icon.setScaledContents(True)
        self.current_weather_icon.setAlignment(Qt.AlignCenter)
        self.current_weather_description = QLabel(self.centralwidget)
        self.current_weather_description.setObjectName(u"current_weather_description")
        self.current_weather_description.setGeometry(QRect(180, 430, 451, 31))
        font4 = QFont()
        font4.setFamilies([u"Papyrus"])
        font4.setPointSize(15)
        self.current_weather_description.setFont(font4)
        self.current_weather_description.setStyleSheet(u"border: none;\n"
"color: rgb(216, 255, 254);")
        self.current_weather_description.setAlignment(Qt.AlignCenter)
        self.province_label = QLabel(self.centralwidget)
        self.province_label.setObjectName(u"province_label")
        self.province_label.setGeometry(QRect(200, 220, 391, 31))
        self.province_label.setFont(font4)
        self.province_label.setStyleSheet(u"border: none;\n"
"color: rgb(216, 255, 254);")
        self.province_label.setAlignment(Qt.AlignCenter)
        self.city_name_label = QLabel(self.centralwidget)
        self.city_name_label.setObjectName(u"city_name_label")
        self.city_name_label.setGeometry(QRect(30, 160, 711, 61))
        font5 = QFont()
        font5.setFamilies([u"Papyrus"])
        font5.setPointSize(25)
        font5.setBold(True)
        self.city_name_label.setFont(font5)
        self.city_name_label.setStyleSheet(u"border: none;\n"
"color: rgb(216, 255, 254);")
        self.city_name_label.setAlignment(Qt.AlignCenter)
        self.population_label = QLabel(self.centralwidget)
        self.population_label.setObjectName(u"population_label")
        self.population_label.setGeometry(QRect(300, 260, 171, 31))
        font6 = QFont()
        font6.setFamilies([u"Papyrus"])
        font6.setPointSize(12)
        self.population_label.setFont(font6)
        self.population_label.setStyleSheet(u"border: none;\n"
"color: rgb(216, 255, 254);")
        self.population_label.setAlignment(Qt.AlignCenter)
        self.label_52 = QLabel(self.centralwidget)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(350, 480, 50, 50))
        self.label_52.setMaximumSize(QSize(50, 50))
        self.label_52.setStyleSheet(u"padding: 5px;\n"
"\n"
"border-radius: 20px;\n"
"color: rgb(252, 191, 130);")
        self.label_52.setPixmap(QPixmap(u"icons/thermometer.png"))
        self.label_52.setScaledContents(True)
        self.label_57 = QLabel(self.centralwidget)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(550, 480, 50, 50))
        self.label_57.setMaximumSize(QSize(50, 50))
        self.label_57.setStyleSheet(u"padding: 5px;\n"
"\n"
"border-radius: 20px;\n"
"color: rgb(252, 191, 130);")
        self.label_57.setPixmap(QPixmap(u"icons/humidty.png"))
        self.label_57.setScaledContents(True)
        self.label_50 = QLabel(self.centralwidget)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(140, 480, 50, 50))
        self.label_50.setMaximumSize(QSize(50, 50))
        font7 = QFont()
        font7.setPointSize(42)
        self.label_50.setFont(font7)
        self.label_50.setStyleSheet(u"padding: 5px;\n"
"\n"
"border-radius: 20px;\n"
"color: rgb(252, 191, 130);")
        self.label_50.setPixmap(QPixmap(u"icons/wind.png"))
        self.label_50.setScaledContents(True)
        self.forecast_time1_8 = QLabel(self.centralwidget)
        self.forecast_time1_8.setObjectName(u"forecast_time1_8")
        self.forecast_time1_8.setGeometry(QRect(50, 540, 131, 41))
        self.forecast_time1_8.setMinimumSize(QSize(0, 30))
        font8 = QFont()
        font8.setFamilies([u"Papyrus"])
        font8.setPointSize(14)
        font8.setBold(True)
        font8.setItalic(False)
        self.forecast_time1_8.setFont(font8)
        self.forecast_time1_8.setStyleSheet(u"\n"
"border: none;\n"
"color: rgb(170, 119, 138);")
        self.forecast_time1_8.setAlignment(Qt.AlignCenter)
        self.forecast_temp_3hours = QLabel(self.centralwidget)
        self.forecast_temp_3hours.setObjectName(u"forecast_temp_3hours")
        self.forecast_temp_3hours.setGeometry(QRect(90, 570, 101, 51))
        self.forecast_temp_3hours.setMinimumSize(QSize(0, 30))
        font9 = QFont()
        font9.setFamilies([u"Papyrus"])
        font9.setPointSize(12)
        font9.setBold(False)
        font9.setItalic(False)
        self.forecast_temp_3hours.setFont(font9)
        self.forecast_temp_3hours.setStyleSheet(u"font: 12pt \"Papyrus\";\n"
"color: rgb(216, 255, 254);")
        self.forecast_icon_3hours = QLabel(self.centralwidget)
        self.forecast_icon_3hours.setObjectName(u"forecast_icon_3hours")
        self.forecast_icon_3hours.setGeometry(QRect(40, 570, 50, 50))
        self.forecast_icon_3hours.setMinimumSize(QSize(50, 50))
        self.forecast_icon_3hours.setMaximumSize(QSize(50, 50))
        font10 = QFont()
        font10.setPointSize(8)
        self.forecast_icon_3hours.setFont(font10)
        self.forecast_icon_3hours.setStyleSheet(u"border: none;\n"
"padding: 5px;\n"
"\n"
"border-radius: 25px;\n"
"color: rgb(252, 191, 130);")
        self.forecast_icon_3hours.setScaledContents(True)
        self.forecast_time1_9 = QLabel(self.centralwidget)
        self.forecast_time1_9.setObjectName(u"forecast_time1_9")
        self.forecast_time1_9.setGeometry(QRect(220, 540, 131, 41))
        self.forecast_time1_9.setMinimumSize(QSize(0, 30))
        font11 = QFont()
        font11.setFamilies([u"Papyrus"])
        font11.setPointSize(12)
        font11.setBold(True)
        self.forecast_time1_9.setFont(font11)
        self.forecast_time1_9.setStyleSheet(u"border: none;\n"
"color: rgb(170, 119, 138);")
        self.forecast_time1_9.setAlignment(Qt.AlignCenter)
        self.forecast_time1_10 = QLabel(self.centralwidget)
        self.forecast_time1_10.setObjectName(u"forecast_time1_10")
        self.forecast_time1_10.setGeometry(QRect(390, 540, 131, 41))
        self.forecast_time1_10.setMinimumSize(QSize(0, 30))
        font12 = QFont()
        font12.setFamilies([u"Papyrus"])
        font12.setPointSize(12)
        font12.setBold(True)
        font12.setItalic(False)
        self.forecast_time1_10.setFont(font12)
        self.forecast_time1_10.setStyleSheet(u"border: none;\n"
"color: rgb(170, 119, 138);")
        self.forecast_time1_10.setAlignment(Qt.AlignCenter)
        self.forecast_time1_11 = QLabel(self.centralwidget)
        self.forecast_time1_11.setObjectName(u"forecast_time1_11")
        self.forecast_time1_11.setGeometry(QRect(580, 540, 131, 41))
        self.forecast_time1_11.setMinimumSize(QSize(0, 30))
        self.forecast_time1_11.setFont(font11)
        self.forecast_time1_11.setStyleSheet(u"border: none;\n"
"color: rgb(170, 119, 138);")
        self.forecast_time1_11.setAlignment(Qt.AlignCenter)
        self.forecast_icon_6hours = QLabel(self.centralwidget)
        self.forecast_icon_6hours.setObjectName(u"forecast_icon_6hours")
        self.forecast_icon_6hours.setGeometry(QRect(210, 570, 50, 50))
        self.forecast_icon_6hours.setMinimumSize(QSize(50, 50))
        self.forecast_icon_6hours.setMaximumSize(QSize(50, 50))
        self.forecast_icon_6hours.setFont(font10)
        self.forecast_icon_6hours.setStyleSheet(u"border: none;\n"
"padding: 5px;\n"
"\n"
"border-radius: 25px;\n"
"color: rgb(252, 191, 130);")
        self.forecast_icon_6hours.setScaledContents(True)
        self.forecast_temp_6hours = QLabel(self.centralwidget)
        self.forecast_temp_6hours.setObjectName(u"forecast_temp_6hours")
        self.forecast_temp_6hours.setGeometry(QRect(260, 570, 91, 51))
        self.forecast_temp_6hours.setMinimumSize(QSize(0, 30))
        self.forecast_temp_6hours.setFont(font9)
        self.forecast_temp_6hours.setStyleSheet(u"font: 12pt \"Papyrus\";\n"
"color: rgb(216, 255, 254);")
        self.forecast_icon_9hours = QLabel(self.centralwidget)
        self.forecast_icon_9hours.setObjectName(u"forecast_icon_9hours")
        self.forecast_icon_9hours.setGeometry(QRect(380, 570, 50, 50))
        self.forecast_icon_9hours.setMinimumSize(QSize(50, 50))
        self.forecast_icon_9hours.setMaximumSize(QSize(50, 50))
        self.forecast_icon_9hours.setFont(font10)
        self.forecast_icon_9hours.setStyleSheet(u"border: none;\n"
"padding: 5px;\n"
"\n"
"border-radius: 25px;\n"
"color: rgb(252, 191, 130);")
        self.forecast_icon_9hours.setScaledContents(True)
        self.forecast_temp_9hours = QLabel(self.centralwidget)
        self.forecast_temp_9hours.setObjectName(u"forecast_temp_9hours")
        self.forecast_temp_9hours.setGeometry(QRect(430, 570, 91, 51))
        self.forecast_temp_9hours.setMinimumSize(QSize(0, 30))
        self.forecast_temp_9hours.setFont(font9)
        self.forecast_temp_9hours.setStyleSheet(u"font: 12pt \"Papyrus\";\n"
"color: rgb(216, 255, 254);")
        self.forecast_icon_12hours = QLabel(self.centralwidget)
        self.forecast_icon_12hours.setObjectName(u"forecast_icon_12hours")
        self.forecast_icon_12hours.setGeometry(QRect(570, 570, 50, 50))
        self.forecast_icon_12hours.setMinimumSize(QSize(50, 50))
        self.forecast_icon_12hours.setMaximumSize(QSize(50, 50))
        self.forecast_icon_12hours.setFont(font10)
        self.forecast_icon_12hours.setStyleSheet(u"border: none;\n"
"padding: 5px;\n"
"\n"
"border-radius: 25px;\n"
"color: rgb(252, 191, 130);")
        self.forecast_icon_12hours.setScaledContents(True)
        self.forecast_temp_12hours = QLabel(self.centralwidget)
        self.forecast_temp_12hours.setObjectName(u"forecast_temp_12hours")
        self.forecast_temp_12hours.setGeometry(QRect(620, 570, 91, 51))
        self.forecast_temp_12hours.setMinimumSize(QSize(0, 30))
        self.forecast_temp_12hours.setFont(font9)
        self.forecast_temp_12hours.setStyleSheet(u"font: 12pt \"Papyrus\";\n"
"color: rgb(216, 255, 254);")
        self.forecast_icon_tomorrow = QLabel(self.centralwidget)
        self.forecast_icon_tomorrow.setObjectName(u"forecast_icon_tomorrow")
        self.forecast_icon_tomorrow.setGeometry(QRect(80, 690, 50, 50))
        self.forecast_icon_tomorrow.setMinimumSize(QSize(50, 50))
        self.forecast_icon_tomorrow.setMaximumSize(QSize(50, 50))
        self.forecast_icon_tomorrow.setFont(font10)
        self.forecast_icon_tomorrow.setStyleSheet(u"border: none;\n"
"padding: 5px;\n"
"\n"
"border-radius: 25px;\n"
"color: rgb(252, 191, 130);")
        self.forecast_icon_tomorrow.setScaledContents(True)
        self.forecast_time1_12 = QLabel(self.centralwidget)
        self.forecast_time1_12.setObjectName(u"forecast_time1_12")
        self.forecast_time1_12.setGeometry(QRect(90, 650, 131, 41))
        self.forecast_time1_12.setMinimumSize(QSize(0, 30))
        font13 = QFont()
        font13.setFamilies([u"Papyrus"])
        font13.setPointSize(14)
        font13.setBold(True)
        self.forecast_time1_12.setFont(font13)
        self.forecast_time1_12.setStyleSheet(u"border: none;\n"
"color: rgb(170, 119, 138);")
        self.forecast_time1_12.setAlignment(Qt.AlignCenter)
        self.forecast_temp_tomorrow = QLabel(self.centralwidget)
        self.forecast_temp_tomorrow.setObjectName(u"forecast_temp_tomorrow")
        self.forecast_temp_tomorrow.setGeometry(QRect(130, 690, 121, 51))
        self.forecast_temp_tomorrow.setMinimumSize(QSize(0, 30))
        font14 = QFont()
        font14.setFamilies([u"Papyrus"])
        font14.setPointSize(14)
        font14.setBold(False)
        font14.setItalic(False)
        self.forecast_temp_tomorrow.setFont(font14)
        self.forecast_temp_tomorrow.setStyleSheet(u"font: 14pt \"Papyrus\";\n"
"color: rgb(216, 255, 254);")
        self.forecast_icon_after1 = QLabel(self.centralwidget)
        self.forecast_icon_after1.setObjectName(u"forecast_icon_after1")
        self.forecast_icon_after1.setGeometry(QRect(280, 690, 50, 50))
        self.forecast_icon_after1.setMinimumSize(QSize(50, 50))
        self.forecast_icon_after1.setMaximumSize(QSize(50, 50))
        self.forecast_icon_after1.setFont(font10)
        self.forecast_icon_after1.setStyleSheet(u"border: none;\n"
"padding: 5px;\n"
"\n"
"border-radius: 25px;\n"
"color: rgb(252, 191, 130);")
        self.forecast_icon_after1.setScaledContents(True)
        self.forecast_temp_after1 = QLabel(self.centralwidget)
        self.forecast_temp_after1.setObjectName(u"forecast_temp_after1")
        self.forecast_temp_after1.setGeometry(QRect(330, 690, 121, 51))
        self.forecast_temp_after1.setMinimumSize(QSize(0, 30))
        self.forecast_temp_after1.setFont(font14)
        self.forecast_temp_after1.setStyleSheet(u"font: 14pt \"Papyrus\";\n"
"color: rgb(216, 255, 254);")
        self.forecast_time1_13 = QLabel(self.centralwidget)
        self.forecast_time1_13.setObjectName(u"forecast_time1_13")
        self.forecast_time1_13.setGeometry(QRect(290, 650, 151, 41))
        self.forecast_time1_13.setMinimumSize(QSize(0, 30))
        self.forecast_time1_13.setFont(font13)
        self.forecast_time1_13.setStyleSheet(u"border: none;\n"
"color: rgb(170, 119, 138);")
        self.forecast_time1_13.setAlignment(Qt.AlignCenter)
        self.forecast_icon_after2 = QLabel(self.centralwidget)
        self.forecast_icon_after2.setObjectName(u"forecast_icon_after2")
        self.forecast_icon_after2.setGeometry(QRect(480, 690, 50, 50))
        self.forecast_icon_after2.setMinimumSize(QSize(50, 50))
        self.forecast_icon_after2.setMaximumSize(QSize(50, 50))
        self.forecast_icon_after2.setFont(font10)
        self.forecast_icon_after2.setStyleSheet(u"border: none;\n"
"padding: 5px;\n"
"\n"
"border-radius: 25px;\n"
"color: rgb(252, 191, 130);")
        self.forecast_icon_after2.setScaledContents(True)
        self.forecast_temp_after2 = QLabel(self.centralwidget)
        self.forecast_temp_after2.setObjectName(u"forecast_temp_after2")
        self.forecast_temp_after2.setGeometry(QRect(530, 690, 121, 51))
        self.forecast_temp_after2.setMinimumSize(QSize(0, 30))
        self.forecast_temp_after2.setFont(font14)
        self.forecast_temp_after2.setStyleSheet(u"font: 14pt \"Papyrus\";\n"
"color: rgb(216, 255, 254);")
        self.forecast_time1_14 = QLabel(self.centralwidget)
        self.forecast_time1_14.setObjectName(u"forecast_time1_14")
        self.forecast_time1_14.setGeometry(QRect(490, 650, 151, 41))
        self.forecast_time1_14.setMinimumSize(QSize(0, 30))
        self.forecast_time1_14.setFont(font13)
        self.forecast_time1_14.setStyleSheet(u"border: none;\n"
"color: rgb(170, 119, 138);")
        self.forecast_time1_14.setAlignment(Qt.AlignCenter)
        self.temperature_label = QLabel(self.centralwidget)
        self.temperature_label.setObjectName(u"temperature_label")
        self.temperature_label.setGeometry(QRect(210, 290, 341, 141))
        font15 = QFont()
        font15.setFamilies([u"Papyrus"])
        font15.setPointSize(60)
        self.temperature_label.setFont(font15)
        self.temperature_label.setStyleSheet(u"border: none;\n"
"color: rgb(216, 255, 254);")
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.label_51 = QLabel(self.centralwidget)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(500, 320, 75, 75))
        self.label_51.setMaximumSize(QSize(75, 75))
        self.label_51.setStyleSheet(u"padding: 5px;\n"
"\n"
"border-radius: 20px;\n"
"color: rgb(252, 191, 130);")
        self.label_51.setPixmap(QPixmap(u"icons/hot.png"))
        self.label_51.setScaledContents(True)
        self.wind_speed_label = QLabel(self.centralwidget)
        self.wind_speed_label.setObjectName(u"wind_speed_label")
        self.wind_speed_label.setGeometry(QRect(190, 490, 101, 31))
        font16 = QFont()
        font16.setFamilies([u"Papyrus"])
        font16.setPointSize(15)
        font16.setBold(False)
        font16.setItalic(False)
        self.wind_speed_label.setFont(font16)
        self.wind_speed_label.setStyleSheet(u"\n"
"color: rgb(216, 255, 254);")
        self.pressure_label = QLabel(self.centralwidget)
        self.pressure_label.setObjectName(u"pressure_label")
        self.pressure_label.setGeometry(QRect(400, 490, 121, 31))
        self.pressure_label.setFont(font16)
        self.pressure_label.setStyleSheet(u"\n"
"color: rgb(216, 255, 254);")
        self.pressure_label_3 = QLabel(self.centralwidget)
        self.pressure_label_3.setObjectName(u"pressure_label_3")
        self.pressure_label_3.setGeometry(QRect(600, 480, 51, 41))
        self.pressure_label_3.setFont(font16)
        self.pressure_label_3.setStyleSheet(u"\n"
"color: rgb(216, 255, 254);")
        self.cities_list = QComboBox(self.centralwidget)
        self.cities_list.setObjectName(u"cities_list")
        self.cities_list.setGeometry(QRect(370, 60, 371, 38))
        self.cities_list.setFont(font1)
        self.cities_list.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid rgb(103, 103, 103);\n"
"border-radius: 10px;\n"
"color: rgb(272, 191, 130);")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(154, 192, 214));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(200, 750, 371, 101))
        self.tableWidget.setStyleSheet(u"background-color: rgb(154, 192, 214);\n"
"background-color: rgb(154, 192, 214);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.countries_list.raise_()
        self.search_city.raise_()
        self.current_weather_description.raise_()
        self.province_label.raise_()
        self.city_name_label.raise_()
        self.population_label.raise_()
        self.label_52.raise_()
        self.label_57.raise_()
        self.label_50.raise_()
        self.forecast_time1_8.raise_()
        self.forecast_temp_3hours.raise_()
        self.forecast_icon_3hours.raise_()
        self.forecast_time1_9.raise_()
        self.forecast_time1_10.raise_()
        self.forecast_time1_11.raise_()
        self.forecast_icon_6hours.raise_()
        self.forecast_temp_6hours.raise_()
        self.forecast_icon_9hours.raise_()
        self.forecast_temp_9hours.raise_()
        self.forecast_icon_12hours.raise_()
        self.forecast_temp_12hours.raise_()
        self.forecast_icon_tomorrow.raise_()
        self.forecast_time1_12.raise_()
        self.forecast_temp_tomorrow.raise_()
        self.forecast_icon_after1.raise_()
        self.forecast_temp_after1.raise_()
        self.forecast_time1_13.raise_()
        self.forecast_icon_after2.raise_()
        self.forecast_temp_after2.raise_()
        self.forecast_time1_14.raise_()
        self.temperature_label.raise_()
        self.current_weather_icon.raise_()
        self.label_51.raise_()
        self.wind_speed_label.raise_()
        self.pressure_label.raise_()
        self.pressure_label_3.raise_()
        self.cities_list.raise_()
        self.tableWidget.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 750, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.countries_list.setCurrentIndex(-1)
        self.cities_list.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Weather-Vista", None))
        self.countries_list.setCurrentText("")
        self.search_city.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Here \ud83d\udd0e", None))
        self.current_weather_icon.setText("")
        self.current_weather_description.setText(QCoreApplication.translate("MainWindow", u"Current Weather Descriptions Here", None))
        self.province_label.setText(QCoreApplication.translate("MainWindow", u"Province Name", None))
        self.city_name_label.setText(QCoreApplication.translate("MainWindow", u"City Name", None))
        self.population_label.setText(QCoreApplication.translate("MainWindow", u"Population", None))
        self.label_52.setText("")
        self.label_57.setText("")
        self.label_50.setText("")
        self.forecast_time1_8.setText(QCoreApplication.translate("MainWindow", u"+3 Hours", None))
        self.forecast_temp_3hours.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.forecast_icon_3hours.setText("")
        self.forecast_time1_9.setText(QCoreApplication.translate("MainWindow", u"+6 Hours", None))
        self.forecast_time1_10.setText(QCoreApplication.translate("MainWindow", u"+9 Hours", None))
        self.forecast_time1_11.setText(QCoreApplication.translate("MainWindow", u"+12 Hours", None))
        self.forecast_icon_6hours.setText("")
        self.forecast_temp_6hours.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.forecast_icon_9hours.setText("")
        self.forecast_temp_9hours.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.forecast_icon_12hours.setText("")
        self.forecast_temp_12hours.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.forecast_icon_tomorrow.setText("")
        self.forecast_time1_12.setText(QCoreApplication.translate("MainWindow", u"Tomorrow", None))
        self.forecast_temp_tomorrow.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.forecast_icon_after1.setText("")
        self.forecast_temp_after1.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.forecast_time1_13.setText(QCoreApplication.translate("MainWindow", u"Tomorrow +1", None))
        self.forecast_icon_after2.setText("")
        self.forecast_temp_after2.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.forecast_time1_14.setText(QCoreApplication.translate("MainWindow", u"Tomorrow +2", None))
        self.temperature_label.setText(QCoreApplication.translate("MainWindow", u"27 c", None))
        self.label_51.setText("")
        self.wind_speed_label.setText(QCoreApplication.translate("MainWindow", u"113 km/h", None))
        self.pressure_label.setText(QCoreApplication.translate("MainWindow", u"1.029 hPa", None))
        self.pressure_label_3.setText(QCoreApplication.translate("MainWindow", u"%78", None))
        self.cities_list.setCurrentText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"City Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Province", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Population", None));
    # retranslateUi

