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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1490, 820)
        MainWindow.setStyleSheet(u"background-color: rgb(154, 192, 214);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.weather_forecast_frame_9 = QFrame(self.centralwidget)
        self.weather_forecast_frame_9.setObjectName(u"weather_forecast_frame_9")
        self.weather_forecast_frame_9.setEnabled(True)
        self.weather_forecast_frame_9.setGeometry(QRect(379, 447, 1101, 171))
        font = QFont()
        font.setKerning(True)
        self.weather_forecast_frame_9.setFont(font)
        self.weather_forecast_frame_9.setStyleSheet(u"QFrame{border-top: 2px solid rgb(154, 148, 196)}")
        self.weather_forecast_frame_9.setFrameShape(QFrame.StyledPanel)
        self.weather_forecast_frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.weather_forecast_frame_9)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_30.setContentsMargins(7, 7, 4, 7)
        self.frame_53 = QFrame(self.weather_forecast_frame_9)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setStyleSheet(u"background-color: rgb(190, 199, 229);\n"
"background-color: rgb(154, 192, 214);\n"
"padding: 10px;\n"
"border-radius: 20px;\n"
"border: none;")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.gridLayout_57 = QGridLayout(self.frame_53)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.forecast_temp_3hours = QLabel(self.frame_53)
        self.forecast_temp_3hours.setObjectName(u"forecast_temp_3hours")
        self.forecast_temp_3hours.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamilies([u"Sitka Banner"])
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setItalic(False)
        self.forecast_temp_3hours.setFont(font1)
        self.forecast_temp_3hours.setStyleSheet(u"font: 18pt \"Sitka Banner\";\n"
"color: rgb(216, 255, 254);")

        self.gridLayout_57.addWidget(self.forecast_temp_3hours, 1, 1, 1, 1)

        self.forecast_icon_3hours = QLabel(self.frame_53)
        self.forecast_icon_3hours.setObjectName(u"forecast_icon_3hours")
        self.forecast_icon_3hours.setMinimumSize(QSize(50, 50))
        self.forecast_icon_3hours.setMaximumSize(QSize(50, 50))
        font2 = QFont()
        font2.setPointSize(8)
        self.forecast_icon_3hours.setFont(font2)
        self.forecast_icon_3hours.setStyleSheet(u"border: none;\n"
"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 25px;\n"
"color: rgb(252, 191, 130);")
        self.forecast_icon_3hours.setPixmap(QPixmap(u":/weather/icons/weather/png/030-weather app.png"))
        self.forecast_icon_3hours.setScaledContents(True)

        self.gridLayout_57.addWidget(self.forecast_icon_3hours, 1, 0, 1, 1)

        self.forecast_time1_8 = QLabel(self.frame_53)
        self.forecast_time1_8.setObjectName(u"forecast_time1_8")
        self.forecast_time1_8.setMinimumSize(QSize(0, 30))
        font3 = QFont()
        font3.setFamilies([u"Adobe Caslon Pro"])
        font3.setPointSize(12)
        self.forecast_time1_8.setFont(font3)
        self.forecast_time1_8.setStyleSheet(u"border: none;\n"
"color: rgb(170, 119, 138);")
        self.forecast_time1_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_57.addWidget(self.forecast_time1_8, 0, 0, 1, 2)


        self.horizontalLayout_30.addWidget(self.frame_53)

        self.frame_54 = QFrame(self.weather_forecast_frame_9)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setStyleSheet(u"background-color: rgb(190, 199, 229);\n"
"background-color: rgb(154, 192, 214);\n"
"padding: 10px;\n"
"border-radius: 20px;\n"
"border: none;")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.gridLayout_58 = QGridLayout(self.frame_54)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.forecast_temp_6hours = QLabel(self.frame_54)
        self.forecast_temp_6hours.setObjectName(u"forecast_temp_6hours")
        self.forecast_temp_6hours.setMinimumSize(QSize(0, 30))
        self.forecast_temp_6hours.setFont(font1)
        self.forecast_temp_6hours.setStyleSheet(u"font: 18pt \"Sitka Banner\";\n"
"color: rgb(216, 255, 254);")

        self.gridLayout_58.addWidget(self.forecast_temp_6hours, 1, 1, 1, 1)

        self.forecast_icon_6hours = QLabel(self.frame_54)
        self.forecast_icon_6hours.setObjectName(u"forecast_icon_6hours")
        self.forecast_icon_6hours.setMinimumSize(QSize(50, 50))
        self.forecast_icon_6hours.setMaximumSize(QSize(50, 50))
        self.forecast_icon_6hours.setFont(font2)
        self.forecast_icon_6hours.setStyleSheet(u"border: none;\n"
"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 25px;\n"
"color: rgb(252, 191, 130);")
        self.forecast_icon_6hours.setPixmap(QPixmap(u":/weather/icons/weather/png/030-weather app.png"))
        self.forecast_icon_6hours.setScaledContents(True)

        self.gridLayout_58.addWidget(self.forecast_icon_6hours, 1, 0, 1, 1)

        self.forecast_time2_8 = QLabel(self.frame_54)
        self.forecast_time2_8.setObjectName(u"forecast_time2_8")
        self.forecast_time2_8.setMinimumSize(QSize(0, 30))
        self.forecast_time2_8.setFont(font3)
        self.forecast_time2_8.setStyleSheet(u"border: none;\n"
"color: rgb(170, 119, 138);")
        self.forecast_time2_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_58.addWidget(self.forecast_time2_8, 0, 0, 1, 2)


        self.horizontalLayout_30.addWidget(self.frame_54)

        self.frame_55 = QFrame(self.weather_forecast_frame_9)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setStyleSheet(u"background-color: rgb(190, 199, 229);\n"
"background-color: rgb(154, 192, 214);\n"
"padding: 10px;\n"
"border-radius: 20px;\n"
"border: none;")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.gridLayout_59 = QGridLayout(self.frame_55)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.forecast_icon_9hours = QLabel(self.frame_55)
        self.forecast_icon_9hours.setObjectName(u"forecast_icon_9hours")
        self.forecast_icon_9hours.setMinimumSize(QSize(50, 50))
        self.forecast_icon_9hours.setMaximumSize(QSize(50, 50))
        self.forecast_icon_9hours.setFont(font2)
        self.forecast_icon_9hours.setStyleSheet(u"border: none;\n"
"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 25px;\n"
"color: rgb(252, 191, 130);")
        self.forecast_icon_9hours.setPixmap(QPixmap(u":/weather/icons/weather/png/030-weather app.png"))
        self.forecast_icon_9hours.setScaledContents(True)

        self.gridLayout_59.addWidget(self.forecast_icon_9hours, 1, 0, 1, 1)

        self.forecast_time3_12 = QLabel(self.frame_55)
        self.forecast_time3_12.setObjectName(u"forecast_time3_12")
        self.forecast_time3_12.setMinimumSize(QSize(0, 30))
        self.forecast_time3_12.setFont(font3)
        self.forecast_time3_12.setStyleSheet(u"border: none;\n"
"color: rgb(170, 119, 138);")
        self.forecast_time3_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_59.addWidget(self.forecast_time3_12, 0, 0, 1, 2)

        self.forecast_temp_9hours = QLabel(self.frame_55)
        self.forecast_temp_9hours.setObjectName(u"forecast_temp_9hours")
        self.forecast_temp_9hours.setMinimumSize(QSize(0, 30))
        self.forecast_temp_9hours.setFont(font1)
        self.forecast_temp_9hours.setStyleSheet(u"font: 18pt \"Sitka Banner\";\n"
"color: rgb(216, 255, 254);")

        self.gridLayout_59.addWidget(self.forecast_temp_9hours, 1, 1, 1, 1)


        self.horizontalLayout_30.addWidget(self.frame_55)

        self.frame_56 = QFrame(self.weather_forecast_frame_9)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setStyleSheet(u"background-color: rgb(190, 199, 229);\n"
"background-color: rgb(154, 192, 214);\n"
"padding: 10px;\n"
"border-radius: 20px;\n"
"border: none;")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.gridLayout_60 = QGridLayout(self.frame_56)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.forecast_icon_12hours = QLabel(self.frame_56)
        self.forecast_icon_12hours.setObjectName(u"forecast_icon_12hours")
        self.forecast_icon_12hours.setMinimumSize(QSize(50, 50))
        self.forecast_icon_12hours.setMaximumSize(QSize(50, 50))
        self.forecast_icon_12hours.setFont(font2)
        self.forecast_icon_12hours.setStyleSheet(u"border: none;\n"
"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 25px;\n"
"color: rgb(252, 191, 130);")
        self.forecast_icon_12hours.setPixmap(QPixmap(u":/weather/icons/weather/png/030-weather app.png"))
        self.forecast_icon_12hours.setScaledContents(True)

        self.gridLayout_60.addWidget(self.forecast_icon_12hours, 1, 0, 1, 1)

        self.forecast_temp_12hours = QLabel(self.frame_56)
        self.forecast_temp_12hours.setObjectName(u"forecast_temp_12hours")
        self.forecast_temp_12hours.setMinimumSize(QSize(0, 30))
        self.forecast_temp_12hours.setFont(font1)
        self.forecast_temp_12hours.setStyleSheet(u"font: 18pt \"Sitka Banner\";\n"
"color: rgb(216, 255, 254);")

        self.gridLayout_60.addWidget(self.forecast_temp_12hours, 1, 1, 1, 1)

        self.forecast_time4_12 = QLabel(self.frame_56)
        self.forecast_time4_12.setObjectName(u"forecast_time4_12")
        self.forecast_time4_12.setMinimumSize(QSize(0, 30))
        self.forecast_time4_12.setFont(font3)
        self.forecast_time4_12.setStyleSheet(u"border: none;\n"
"color: rgb(170, 119, 138);")
        self.forecast_time4_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_60.addWidget(self.forecast_time4_12, 0, 0, 1, 2)


        self.horizontalLayout_30.addWidget(self.frame_56)

        self.weather_forecast_frame_10 = QFrame(self.centralwidget)
        self.weather_forecast_frame_10.setObjectName(u"weather_forecast_frame_10")
        self.weather_forecast_frame_10.setGeometry(QRect(380, 630, 1101, 171))
        self.weather_forecast_frame_10.setStyleSheet(u"QFrame{border-top: 2px solid rgb(154, 148, 196)}")
        self.weather_forecast_frame_10.setFrameShape(QFrame.StyledPanel)
        self.weather_forecast_frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.weather_forecast_frame_10)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.frame_57 = QFrame(self.weather_forecast_frame_10)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setStyleSheet(u"background-color: rgb(190, 199, 229);\n"
"background-color: rgb(154, 192, 214);\n"
"padding: 10px;\n"
"border-radius: 20px;\n"
"border: none;")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.gridLayout_61 = QGridLayout(self.frame_57)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.forecast_temp_tomorrow = QLabel(self.frame_57)
        self.forecast_temp_tomorrow.setObjectName(u"forecast_temp_tomorrow")
        self.forecast_temp_tomorrow.setMinimumSize(QSize(0, 30))
        self.forecast_temp_tomorrow.setFont(font1)
        self.forecast_temp_tomorrow.setStyleSheet(u"font: 18pt \"Sitka Banner\";\n"
"color: rgb(216, 255, 254);")

        self.gridLayout_61.addWidget(self.forecast_temp_tomorrow, 1, 1, 1, 1)

        self.forecast_icon_tomorrow = QLabel(self.frame_57)
        self.forecast_icon_tomorrow.setObjectName(u"forecast_icon_tomorrow")
        self.forecast_icon_tomorrow.setMinimumSize(QSize(50, 50))
        self.forecast_icon_tomorrow.setMaximumSize(QSize(50, 50))
        self.forecast_icon_tomorrow.setFont(font2)
        self.forecast_icon_tomorrow.setStyleSheet(u"border: none;\n"
"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 25px;\n"
"color: rgb(252, 191, 130);")
        self.forecast_icon_tomorrow.setPixmap(QPixmap(u":/weather/icons/weather/png/030-weather app.png"))
        self.forecast_icon_tomorrow.setScaledContents(True)

        self.gridLayout_61.addWidget(self.forecast_icon_tomorrow, 1, 0, 1, 1)

        self.label_tomorrow = QLabel(self.frame_57)
        self.label_tomorrow.setObjectName(u"label_tomorrow")
        self.label_tomorrow.setMinimumSize(QSize(0, 30))
        self.label_tomorrow.setFont(font3)
        self.label_tomorrow.setStyleSheet(u"border: none;\n"
"color: rgb(170, 119, 138);")
        self.label_tomorrow.setAlignment(Qt.AlignCenter)

        self.gridLayout_61.addWidget(self.label_tomorrow, 0, 0, 1, 2)


        self.horizontalLayout_31.addWidget(self.frame_57)

        self.frame_58 = QFrame(self.weather_forecast_frame_10)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setStyleSheet(u"background-color: rgb(190, 199, 229);\n"
"background-color: rgb(154, 192, 214);\n"
"padding: 10px;\n"
"border-radius: 20px;\n"
"border: none;")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.gridLayout_62 = QGridLayout(self.frame_58)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.forecast_icon_after1 = QLabel(self.frame_58)
        self.forecast_icon_after1.setObjectName(u"forecast_icon_after1")
        self.forecast_icon_after1.setMinimumSize(QSize(50, 50))
        self.forecast_icon_after1.setMaximumSize(QSize(50, 50))
        self.forecast_icon_after1.setFont(font2)
        self.forecast_icon_after1.setStyleSheet(u"border: none;\n"
"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 25px;\n"
"color: rgb(252, 191, 130);")
        self.forecast_icon_after1.setPixmap(QPixmap(u":/weather/icons/weather/png/030-weather app.png"))
        self.forecast_icon_after1.setScaledContents(True)

        self.gridLayout_62.addWidget(self.forecast_icon_after1, 1, 0, 1, 1)

        self.forecast_temp_after1 = QLabel(self.frame_58)
        self.forecast_temp_after1.setObjectName(u"forecast_temp_after1")
        self.forecast_temp_after1.setMinimumSize(QSize(0, 30))
        self.forecast_temp_after1.setFont(font1)
        self.forecast_temp_after1.setStyleSheet(u"font: 18pt \"Sitka Banner\";\n"
"color: rgb(216, 255, 254);")

        self.gridLayout_62.addWidget(self.forecast_temp_after1, 1, 1, 1, 1)

        self.label1_tomorrow = QLabel(self.frame_58)
        self.label1_tomorrow.setObjectName(u"label1_tomorrow")
        self.label1_tomorrow.setMinimumSize(QSize(0, 30))
        self.label1_tomorrow.setFont(font3)
        self.label1_tomorrow.setStyleSheet(u"border: none;\n"
"color: rgb(170, 119, 138);")
        self.label1_tomorrow.setAlignment(Qt.AlignCenter)

        self.gridLayout_62.addWidget(self.label1_tomorrow, 0, 0, 1, 2)


        self.horizontalLayout_31.addWidget(self.frame_58)

        self.frame_59 = QFrame(self.weather_forecast_frame_10)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setStyleSheet(u"background-color: rgb(190, 199, 229);\n"
"background-color: rgb(154, 192, 214);\n"
"padding: 10px;\n"
"border-radius: 20px;\n"
"border: none;")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.gridLayout_63 = QGridLayout(self.frame_59)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.forecast_temp_after2 = QLabel(self.frame_59)
        self.forecast_temp_after2.setObjectName(u"forecast_temp_after2")
        self.forecast_temp_after2.setMinimumSize(QSize(0, 30))
        self.forecast_temp_after2.setFont(font1)
        self.forecast_temp_after2.setStyleSheet(u"font: 18pt \"Sitka Banner\";\n"
"color: rgb(216, 255, 254);")

        self.gridLayout_63.addWidget(self.forecast_temp_after2, 1, 1, 1, 1)

        self.forecast_icon_after2 = QLabel(self.frame_59)
        self.forecast_icon_after2.setObjectName(u"forecast_icon_after2")
        self.forecast_icon_after2.setMinimumSize(QSize(50, 50))
        self.forecast_icon_after2.setMaximumSize(QSize(50, 50))
        self.forecast_icon_after2.setFont(font2)
        self.forecast_icon_after2.setStyleSheet(u"border: none;\n"
"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 25px;\n"
"color: rgb(252, 191, 130);")
        self.forecast_icon_after2.setPixmap(QPixmap(u":/weather/icons/weather/png/030-weather app.png"))
        self.forecast_icon_after2.setScaledContents(True)

        self.gridLayout_63.addWidget(self.forecast_icon_after2, 1, 0, 1, 1)

        self.label2_tomorrow = QLabel(self.frame_59)
        self.label2_tomorrow.setObjectName(u"label2_tomorrow")
        self.label2_tomorrow.setMinimumSize(QSize(0, 30))
        self.label2_tomorrow.setFont(font3)
        self.label2_tomorrow.setStyleSheet(u"border: none;\n"
"color: rgb(170, 119, 138);")

        self.gridLayout_63.addWidget(self.label2_tomorrow, 0, 0, 1, 2)


        self.horizontalLayout_31.addWidget(self.frame_59)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(379, 170, 1101, 271))
        self.frame.setStyleSheet(u"QFrame{border-top: 2px solid rgb(154, 148, 196)}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.current_weather = QLabel(self.frame)
        self.current_weather.setObjectName(u"current_weather")
        font4 = QFont()
        font4.setFamilies([u"Adobe Garamond Pro Bold"])
        font4.setPointSize(11)
        self.current_weather.setFont(font4)
        self.current_weather.setStyleSheet(u"border: none;\n"
"color: rgb(170, 119, 138);")

        self.verticalLayout_13.addWidget(self.current_weather, 0, Qt.AlignLeft|Qt.AlignTop)

        self.middle_frame = QFrame(self.frame)
        self.middle_frame.setObjectName(u"middle_frame")
        self.middle_frame.setStyleSheet(u"border: none;\n"
"")
        self.middle_frame.setFrameShape(QFrame.StyledPanel)
        self.middle_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.middle_frame)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.frame_61 = QFrame(self.middle_frame)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(200, 200))
        self.frame_61.setMaximumSize(QSize(200, 200))
        self.frame_61.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 100px;\n"
"color: rgb(252, 191, 130);")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_61)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.current_weather_icon = QLabel(self.frame_61)
        self.current_weather_icon.setObjectName(u"current_weather_icon")
        self.current_weather_icon.setMinimumSize(QSize(100, 100))
        self.current_weather_icon.setMaximumSize(QSize(100, 100))
        font5 = QFont()
        font5.setPointSize(7)
        self.current_weather_icon.setFont(font5)
        self.current_weather_icon.setStyleSheet(u"border: none;\n"
"background: none;")
        self.current_weather_icon.setPixmap(QPixmap(u":/weather/icons/weather/png/027-location.png"))
        self.current_weather_icon.setScaledContents(True)
        self.current_weather_icon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.current_weather_icon)


        self.horizontalLayout_32.addWidget(self.frame_61, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_51 = QLabel(self.middle_frame)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMaximumSize(QSize(50, 50))
        self.label_51.setStyleSheet(u"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 20px;\n"
"color: rgb(252, 191, 130);")
        self.label_51.setPixmap(QPixmap(u"../../Downloads/hot.png"))
        self.label_51.setScaledContents(True)

        self.horizontalLayout_32.addWidget(self.label_51)

        self.temperature_label = QLabel(self.middle_frame)
        self.temperature_label.setObjectName(u"temperature_label")
        font6 = QFont()
        font6.setFamilies([u"Sitka Banner"])
        font6.setPointSize(67)
        font6.setBold(False)
        font6.setItalic(False)
        self.temperature_label.setFont(font6)
        self.temperature_label.setStyleSheet(u"\n"
"font: 67pt \"Sitka Banner\";\n"
"color: rgb(216, 255, 254);")

        self.horizontalLayout_32.addWidget(self.temperature_label)

        self.frame_63 = QFrame(self.middle_frame)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setStyleSheet(u"background-color: rgb(190, 199, 229);\n"
"background-color: rgb(154, 192, 214);\n"
"padding: 10px;\n"
"border-radius: 20px;")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.gridLayout_65 = QGridLayout(self.frame_63)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.wind_speed_label = QLabel(self.frame_63)
        self.wind_speed_label.setObjectName(u"wind_speed_label")
        font7 = QFont()
        font7.setFamilies([u"Sitka Banner"])
        font7.setPointSize(19)
        font7.setBold(False)
        font7.setItalic(False)
        self.wind_speed_label.setFont(font7)
        self.wind_speed_label.setStyleSheet(u"font: 19pt \"Sitka Banner\";\n"
"color: rgb(216, 255, 254);")

        self.gridLayout_65.addWidget(self.wind_speed_label, 0, 1, 1, 1)

        self.label_52 = QLabel(self.frame_63)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(50, 50))
        self.label_52.setStyleSheet(u"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 20px;\n"
"color: rgb(252, 191, 130);")
        self.label_52.setPixmap(QPixmap(u"../../Downloads/thermometer.png"))
        self.label_52.setScaledContents(True)

        self.gridLayout_65.addWidget(self.label_52, 1, 0, 1, 1)

        self.label_50 = QLabel(self.frame_63)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(50, 50))
        font8 = QFont()
        font8.setPointSize(42)
        self.label_50.setFont(font8)
        self.label_50.setStyleSheet(u"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 20px;\n"
"color: rgb(252, 191, 130);")
        self.label_50.setPixmap(QPixmap(u"../../Downloads/wind.png"))
        self.label_50.setScaledContents(True)

        self.gridLayout_65.addWidget(self.label_50, 0, 0, 1, 1)

        self.pressure_label = QLabel(self.frame_63)
        self.pressure_label.setObjectName(u"pressure_label")
        font9 = QFont()
        font9.setFamilies([u"Sitka Banner"])
        font9.setPointSize(20)
        font9.setBold(False)
        font9.setItalic(False)
        self.pressure_label.setFont(font9)
        self.pressure_label.setStyleSheet(u"font: 20pt \"Sitka Banner\";\n"
"color: rgb(216, 255, 254);")

        self.gridLayout_65.addWidget(self.pressure_label, 1, 1, 1, 1)

        self.pressure_label_3 = QLabel(self.frame_63)
        self.pressure_label_3.setObjectName(u"pressure_label_3")
        self.pressure_label_3.setFont(font9)
        self.pressure_label_3.setStyleSheet(u"font: 20pt \"Sitka Banner\";\n"
"color: rgb(216, 255, 254);")

        self.gridLayout_65.addWidget(self.pressure_label_3, 2, 1, 1, 1)

        self.label_57 = QLabel(self.frame_63)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMaximumSize(QSize(50, 50))
        self.label_57.setStyleSheet(u"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 20px;\n"
"color: rgb(252, 191, 130);")
        self.label_57.setPixmap(QPixmap(u"../../Downloads/weather.png"))
        self.label_57.setScaledContents(True)

        self.gridLayout_65.addWidget(self.label_57, 2, 0, 1, 1)


        self.horizontalLayout_32.addWidget(self.frame_63)


        self.verticalLayout_13.addWidget(self.middle_frame, 0, Qt.AlignTop)

        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setGeometry(QRect(0, 60, 1490, 62))
        self.top_frame.setMinimumSize(QSize(882, 62))
        self.top_frame.setMaximumSize(QSize(16777215, 62))
        self.top_frame.setStyleSheet(u"border-bottom: 2px solid rgb(154, 148, 196)")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_66 = QGridLayout(self.top_frame)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.countries_list = QComboBox(self.top_frame)
        self.countries_list.setObjectName(u"countries_list")
        font10 = QFont()
        font10.setFamilies([u"Sitka Banner"])
        font10.setPointSize(14)
        self.countries_list.setFont(font10)
        self.countries_list.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid rgb(103, 103, 103);\n"
"border-radius: 10px;\n"
"color: rgb(272, 191, 130);")

        self.gridLayout_66.addWidget(self.countries_list, 1, 1, 1, 1)

        self.label_54 = QLabel(self.top_frame)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font10)
        self.label_54.setStyleSheet(u"padding: 5px;\n"
"color: rgb(77, 96, 107);\n"
"border: 1px solid rgb(272, 192, 125);\n"
"border-radius: 10px;")

        self.gridLayout_66.addWidget(self.label_54, 1, 0, 1, 1)

        self.cities_list = QComboBox(self.top_frame)
        self.cities_list.setObjectName(u"cities_list")
        self.cities_list.setFont(font10)
        self.cities_list.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid rgb(103, 103, 103);\n"
"border-radius: 10px;\n"
"color: rgb(252, 191, 130);")

        self.gridLayout_66.addWidget(self.cities_list, 1, 3, 1, 1)

        self.label_53 = QLabel(self.top_frame)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font10)
        self.label_53.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid rgb(272, 192, 125);\n"
"border-radius: 10px;\n"
"color: rgb(77, 96, 107);")

        self.gridLayout_66.addWidget(self.label_53, 1, 2, 1, 1)

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
        self.tableWidget.setGeometry(QRect(0, 168, 371, 651))
        self.tableWidget.setStyleSheet(u"background-color: rgb(154, 192, 214);\n"
"background-color: rgb(154, 192, 214);")
        self.city_name_label = QLabel(self.centralwidget)
        self.city_name_label.setObjectName(u"city_name_label")
        self.city_name_label.setGeometry(QRect(0, 130, 1491, 31))
        font11 = QFont()
        font11.setFamilies([u"Open Sans Extrabold"])
        font11.setPointSize(15)
        font11.setBold(False)
        self.city_name_label.setFont(font11)
        self.city_name_label.setStyleSheet(u"")
        self.city_name_label.setAlignment(Qt.AlignCenter)
        self.search_city = QLineEdit(self.centralwidget)
        self.search_city.setObjectName(u"search_city")
        self.search_city.setGeometry(QRect(10, 120, 361, 41))
        self.search_city.setFont(font10)
        self.search_city.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid rgb(272, 192, 125);\n"
"border-radius: 10px;")
        self.region_label = QLabel(self.centralwidget)
        self.region_label.setObjectName(u"region_label")
        self.region_label.setGeometry(QRect(910, 130, 81, 31))
        self.region_label.setMinimumSize(QSize(0, 30))
        self.region_label.setFont(font3)
        self.region_label.setStyleSheet(u"background-color: rgb(190, 199, 229);\n"
"background-color: rgb(154, 192, 214);")
        self.population_label = QLabel(self.centralwidget)
        self.population_label.setObjectName(u"population_label")
        self.population_label.setGeometry(QRect(1120, 130, 101, 31))
        self.population_label.setMinimumSize(QSize(0, 30))
        self.population_label.setFont(font3)
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, -20, 1491, 91))
        font12 = QFont()
        font12.setFamilies([u"Adobe Garamond Pro Bold"])
        font12.setPointSize(25)
        font12.setBold(True)
        self.label_21.setFont(font12)
        self.label_21.setStyleSheet(u"border: none;\n"
"color: rgb(170, 119, 138);\n"
"background-color: rgb(64, 150, 225);\n"
"background-color: rgb(110, 137, 153);\n"
"background-color: rgb(181, 225, 250);\n"
"color: rgb(229, 161, 187);")
        self.label_21.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1490, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.forecast_temp_3hours.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.forecast_icon_3hours.setText(QCoreApplication.translate("MainWindow", u"icon", None))
        self.forecast_time1_8.setText(QCoreApplication.translate("MainWindow", u"+3 Hours", None))
        self.forecast_temp_6hours.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.forecast_icon_6hours.setText(QCoreApplication.translate("MainWindow", u"icon", None))
        self.forecast_time2_8.setText(QCoreApplication.translate("MainWindow", u"+6 Hours", None))
        self.forecast_icon_9hours.setText(QCoreApplication.translate("MainWindow", u"icon", None))
        self.forecast_time3_12.setText(QCoreApplication.translate("MainWindow", u"+9 Hours", None))
        self.forecast_temp_9hours.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.forecast_icon_12hours.setText(QCoreApplication.translate("MainWindow", u"icon", None))
        self.forecast_temp_12hours.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.forecast_time4_12.setText(QCoreApplication.translate("MainWindow", u"+12 Hours", None))
        self.forecast_temp_tomorrow.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.forecast_icon_tomorrow.setText(QCoreApplication.translate("MainWindow", u"icon", None))
        self.label_tomorrow.setText(QCoreApplication.translate("MainWindow", u"Tomorrow", None))
        self.forecast_icon_after1.setText(QCoreApplication.translate("MainWindow", u"icon", None))
        self.forecast_temp_after1.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.label1_tomorrow.setText(QCoreApplication.translate("MainWindow", u"After Tomorrow", None))
        self.forecast_temp_after2.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.forecast_icon_after2.setText(QCoreApplication.translate("MainWindow", u"icon", None))
        self.label2_tomorrow.setText(QCoreApplication.translate("MainWindow", u"+2 Tomorrow", None))
        self.current_weather.setText(QCoreApplication.translate("MainWindow", u"Current Weather:", None))
        self.current_weather_icon.setText(QCoreApplication.translate("MainWindow", u"icon", None))
        self.label_51.setText("")
        self.temperature_label.setText(QCoreApplication.translate("MainWindow", u"27 C", None))
        self.wind_speed_label.setText(QCoreApplication.translate("MainWindow", u"113 km/h", None))
        self.label_52.setText("")
        self.label_50.setText("")
        self.pressure_label.setText(QCoreApplication.translate("MainWindow", u"1.029 hPa", None))
        self.pressure_label_3.setText(QCoreApplication.translate("MainWindow", u"%78", None))
        self.label_57.setText("")
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Select Country", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Select City", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"City Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Regions", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Population", None));
        self.city_name_label.setText(QCoreApplication.translate("MainWindow", u"City Name", None))
        self.search_city.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Here \ud83d\udd0e", None))
        self.region_label.setText(QCoreApplication.translate("MainWindow", u"Region", None))
        self.population_label.setText(QCoreApplication.translate("MainWindow", u"Population", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Wheather-Vista", None))
    # retranslateUi

