"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""

from PySide6 import QtWidgets
from a_threads import SystemInfo

class Sys_inf(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.__initSignals()
        self.getSystemInfo: SystemInfo

    def initUi(self):

        self.spinBoxDelay = QtWidgets.QSpinBox()
        self.spinBoxDelay.setMinimum(5)

        self.plainTextEditCPU = QtWidgets.QPlainTextEdit()
        self.plainTextEditCPU.setReadOnly(True)

        self.plainTextEditRAM = QtWidgets.QPlainTextEdit()
        self.plainTextEditRAM.setReadOnly(True)

        l = QtWidgets.QVBoxLayout()
        l.addWidget(self.spinBoxDelay)
        l.addWidget(self.plainTextEditCPU)
        l.addWidget(self.plainTextEditRAM)

        self.setLayout(l)

    def __initSignals(self):
        self.spinBoxDelay.valueChanged.connect(self.__setDelay)

    def __setDelay(self):
        self.= self.spinBoxDelay.value()

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Sys_inf()

    window.show()

    app.exec()