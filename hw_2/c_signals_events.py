"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во мониторов+
    * Текущее основное окно+
    * Разрешение экрана+
    * На каком экране окно находится
    * Размеры окна+
    * Минимальные размеры окна+
    * Текущее положение (координаты) окна+
    * Координаты центра приложения+
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""

import datetime as datatime
from PySide6 import QtWidgets, QtGui
from ui.c_signals_events_form import Ui_Form

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        """
        Событие изменения размера окна

        :param event: QtGui.QResizeEvent
        :return: None
        """
        # print(QtGui.QGuiApplication.applicationState())
        # print(self.geometry())

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.ui.pushButtonLB.clicked.connect(self.onPushButtonLBClicked)
        self.ui.pushButtonCenter.clicked.connect(self.onPushButtonCenterClicked)
        self.ui.pushButtonLT.clicked.connect(self.onPushButtonLTClicked)
        self.ui.pushButtonRB.clicked.connect(self.onPushButtonRBClicked)
        self.ui.pushButtonRT.clicked.connect(self.onButtonRTClicked)
        self.ui.pushButtonGetData.clicked.connect(self.onButtonGetDataClicked)
        self.ui.pushButtonMoveCoords.clicked.connect(self.onButtonMoveCoordsClicked)


    def onButtonGetDataClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonGetData
        * Кол-во мониторов+
        * Текущее основное окно+
        * Разрешение экрана+
        * На каком экране окно находится
        * Размеры окна+
        * Минимальные размеры окна+
        * Текущее положение (координаты) окна+
        * Координаты центра приложения+
        * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
        :return: None
        """

        self.ui.plainTextEdit.setPlainText(self,'црфееруагсл'
                                           #  f'{datatime.datetime.now()}'
                                           # f' Кол-во мониторов {len(QtGui.QGuiApplication.screens())} '
                                           # f' Текущее основное окно {QtGui.QGuiApplication.primaryScreen()}'
                                           # f' Разрешение экрана {QtGui.QGuiApplication.screens().size()}'
                                           # f' На каком экране окно находится {1}'
                                           # f' Размеры окна {self.size()}'
                                           # f' Минимальные размеры окна {self.minimumSize()}'
                                           # f' Текущее положение (координаты) окна {self.geometry()}'
                                           # f' Координаты центра приложения {self.frameGeometry().center()}'
                                           # f' Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено) {QtGui.QGuiApplication.applicationState()}'
                                           )


    def onButtonMoveCoordsClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLineEdit

        :return: None
        """

        self.plainTextEditLog.setPlainText(self.lineEdit.text())
    def onPushButtonLBClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLineEdit

        :return: None
        """

        self.plainTextEditLog.setPlainText(self.lineEdit.text())

    def onPushButtonCenterClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLineEdit

        :return: None
        """

        self.plainTextEditLog.setPlainText(self.lineEdit.text())

    def onPushButtonLTClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLineEdit

        :return: None
        """

        self.plainTextEditLog.setPlainText(self.lineEdit.text())

    def onPushButtonRBClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLineEdit

        :return: None
        """

        self.plainTextEditLog.setPlainText(self.lineEdit.text())

    def onButtonRTClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLineEdit

        :return: None
        """

        self.plainTextEditLog.setPlainText(self.lineEdit.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
