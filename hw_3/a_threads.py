"""
Модуль в котором содержаться потоки Qt
"""

import time

import requests
import psutil
from PySide6 import QtCore

class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)  # TODO Создайте экземпляр класса Signal и передайте ему в конструктор тип данных передаваемого значения (в текущем случае list)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None  # TODO создайте атрибут класса self.delay = None, для управлением задержкой получения данных
        self.cpu_value = str(
            psutil.cpu_percent())  # TODO с помощью вызова функции cpu_percent() в пакете psutil получите загрузку CPU
        self.ram_value = str(
            psutil.virtual_memory().percent)  # TODO с помощью вызова функции virtual_memory().percent в пакете psutil получите загрузку RAM
        self.systemInfoReceived.emit(
            [self.cpu_value, self.ram_value])  # TODO с помощью метода .emit передайте в виде списка данные о загрузке CPU и RAM

    def run(self) -> None:  # TODO переопределить метод run
        if self.delay is None:  # TODO Если задержка не передана в поток перед его запуском
            self.delay = 1  # TODO то устанавливайте значение 1
        while True:  # TODO Запустите бесконечный цикл получения информации о системе
            cpu_value = str(psutil.cpu_percent())  # TODO с помощью вызова функции cpu_percent() в пакете psutil получите загрузку CPU
            ram_value = str(psutil.virtual_memory().percent) # TODO с помощью вызова функции virtual_memory().percent в пакете psutil получите загрузку RAM
            self.systemInfoReceived.emit([cpu_value,ram_value])  # TODO с помощью метода .emit передайте в виде списка данные о загрузке CPU и RAM
            time.sleep(self.delay)  # TODO с помощью функции .sleep() приостановите выполнение цикла на время self.delay


class WeatherHandler(QtCore.QThread):
    status_code=QtCore.Signal(object)# TODO Пропишите сигналы, которые считаете нужными

    def __init__(self, lat: int, lon: int, parent=None):
        super().__init__(parent)
        self.lon = lon
        self.lat = lat
        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.delay = 10
        self.status = True

    def run(self) -> None:
        if abs(self.lat)>=90 or abs(self.lon)>=90:# TODO настройте метод для корректной работы
            self.status_code.emit("Некорректные координаты")
            return
        while self.status:
            # TODO Примерный код ниже
            response = requests.get(self.__api_url)
            data = response.json()
            self.status_code.emit(data)
            self.sleep(self.delay)


