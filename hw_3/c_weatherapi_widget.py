"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""
from PySide6 import QtWidgets
from a_threads import WeatherHandler

class weth_inf(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.__initSignals()
        self.status = False

    def initUi(self):

        self.lineEditlon = QtWidgets.QLineEdit()
        self.lineEditlon.setPlaceholderText('Введите долготу')
        self.lineEditlat = QtWidgets.QLineEdit()
        self.lineEditlat.setPlaceholderText('Введите ширину')
        self.plainTextEdit=QtWidgets.QPlainTextEdit()
        self.spinBoxDelay = QtWidgets.QSpinBox()
        self.spinBoxDelay.setMinimum(10)

        self.pushButtonHandle = QtWidgets.QPushButton("Запустить")
        self.pushButtonHandle.setCheckable(True)

        l_lat_lon = QtWidgets.QHBoxLayout()
        l_lat_lon.addWidget(self.lineEditlat)
        l_lat_lon.addWidget(self.lineEditlon)
        l= QtWidgets.QVBoxLayout()
        l.addLayout(l_lat_lon)
        l.addWidget(self.spinBoxDelay)
        l.addWidget(self.plainTextEdit)
        l.addWidget(self.pushButtonHandle)

        self.setLayout(l)

    def __initSignals(self):
        self.pushButtonHandle.clicked.connect(self.__onbuttonclik)
        self.spinBoxDelay.valueChanged.connect(self.__setDelay)

    def __setDelay(self, delay) -> None:
        """
        Метод для установки времени задержки обновления сайта

        :param delay: время задержки обновления информации о доступности сайта
        :return: None
        """

        self.getWeatherThread.delay = delay
    def __onButtonClick_ChangeText(self):
        if self.pushButtonHandle.isChecked():
            self.pushButtonHandle.setText("Остановить")
        else:
            self.pushButtonHandle.setText("Запустить")
    def __onbuttonclik(self):
        try:
            if not self.status:
                self.status=True
                lat=int(self.lineEditlat.text())
                lon=int(self.lineEditlon.text())
                self.__startThread(lat,lon)

                self.getWeatherThread.status_code.connect(lambda date: self.plainTextEdit.setPlainText(f'Задержка по времени {self.getWeatherThread.delay}'
                                                                                                       f'\n Погода в точке земли:{str(date)}'))
            else:
                self.status = False
                self.getWeatherThread.status= False
            self.__onButtonClick_ChangeText()
        except Exception as e:
            return print(e.args)


    def __startThread(self, lon,lat):
        self.lineEditlon.setEnabled(False)
        self.lineEditlat.setEnabled(False)
        self.getWeatherThread = WeatherHandler(lat,lon)
        self.getWeatherThread.status = True
        self.getWeatherThread.finished.connect(self.__threadFinished)
        self.getWeatherThread.start()

    def __threadFinished(self):
        self.getWeatherThread = None
        self.lineEditlon.setEnabled(True)
        self.lineEditlat.setEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = weth_inf()
    window.show()

    app.exec()