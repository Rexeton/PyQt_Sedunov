"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings_form.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль+

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)+

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),+
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""
import sys
from PySide6 import QtWidgets,QtGui,QtCore
from ui.d_eventfilter_settings_form import Ui_Form

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.config_settings = QtCore.QSettings("Counter_PyQT")
        self.initSignals()
        self.now_value = self.ui.lcdNumber.value()
        self.ui.dial.installEventFilter(self)
        self.ui.horizontalSlider.installEventFilter(self)
        self.counter = self.config_settings.value("counter", 0)
        self.razryd = self.config_settings.value("razryd", 0)
        self.change_elem(self.counter )
        self.tek_mode_ind = self.razryd
        self.ui.comboBox.setCurrentIndex(self.razryd)

        self.nastroika_lcd()
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Critical)
        self.msg.setText("Ошибка")
        self.msg.setInformativeText('Переполнение экрана при выбранной разрядности')
        self.msg.setWindowTitle("Ошибка")
    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.ui.comboBox.currentTextChanged.connect(self.nastroika_lcd)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Событие закрытия окна

        :param event: QtGui.QCloseEvent
        :return: None
        """

        # Сохранение списка IP-адресов в настройки
        self.config_settings.setValue(
            "counter",self.ui.dial.value())
        self.config_settings.setValue(
            "razryd",self.ui.comboBox.currentIndex())
    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        self.tek_mode_ind=self.ui.comboBox.currentIndex()
        if watched==self.ui.dial and event.type()==QtCore.QEvent.Type.Paint:
            self.change_elem(self.ui.dial.value())
        elif watched==self.ui.horizontalSlider and event.type()==QtCore.QEvent.Type.Paint:
            self.change_elem(self.ui.horizontalSlider.value())

        return super(Window, self).eventFilter(watched, event)
    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None:
        now_value=self.ui.lcdNumber.value()
        new_value=now_value
        if event.text()=='+' and now_value!=100:
            new_value = now_value + 1
        elif event.text()=='-' and now_value!=0:
            new_value = now_value - 1
        if not self.ui.lcdNumber.checkOverflow(new_value):
            self.change_elem(new_value)
    def nastroika_lcd(self):
        self.tek_mode=self.ui.lcdNumber.mode()
        if self.ui.comboBox.currentText()=='dec':
            self.ui.lcdNumber.setDecMode()
        elif self.ui.comboBox.currentText()=='hex':
            self.ui.lcdNumber.setHexMode()
        elif self.ui.comboBox.currentText()=='bin':
            self.ui.lcdNumber.setBinMode()
        elif self.ui.comboBox.currentText()=='oct':
            self.ui.lcdNumber.setOctMode()
        if self.ui.lcdNumber.checkOverflow(self.ui.lcdNumber.value()):
            self.msg.exec()
            self.ui.lcdNumber.setMode(self.tek_mode)
            self.ui.comboBox.setCurrentIndex(self.tek_mode_ind)
    def change_elem(self,new_value):
        self.ui.dial.setValue(new_value)
        self.ui.lcdNumber.display(new_value)
        self.ui.horizontalSlider.setValue(new_value)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
