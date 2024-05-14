"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.+
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
        self.initSignals()
        self.max_x=0
        self.max_y=0
        for screen in QtGui.QGuiApplication.screens():
            self.max_x+=screen.size().width()
            self.max_y += screen.size().height()
        self.ui.spinBoxX.setMaximum(self.max_x)
        self.ui.spinBoxY.setMaximum(self.max_y)
        self.ui.spinBoxX.setMinimum(-1000)
        self.ui.spinBoxY.setMinimum(-1000)
        self.ui.spinBoxX.setValue(self.geometry().x())
        self.ui.spinBoxY.setValue(self.geometry().y())

    def peremesh(self,wx,wy,nx,ny):
        self.ui.plainTextEdit.setPlainText(f'{datatime.datetime.now()} \n'
                                           f'Произошло перемещение окна\n'
                                           f'С координат х:{wx}, у:{wy}\n'
                                           f'В координаты х:{nx}, у:{ny}')
    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        """
        Событие движения окна

        :param event: QtGui.QMoveEvent
        :return: None
        """
        self.ui.spinBoxX.setValue(self.geometry().x())
        self.ui.spinBoxY.setValue(self.geometry().y())

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        """
        Событие изменения размера окна

        :param event: QtGui.QResizeEvent
        :return: None
        """
        self.ui.plainTextEdit.setPlainText(f'{datatime.datetime.now()} \n'
                                           f'Текущий размер ширина: {self.geometry().width()}, высота:{self.geometry().height()}')

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
        * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)!
        :return: None
        """


        self.ui.plainTextEdit.setPlainText(
                                           f'{datatime.datetime.now()} \n'
                                           f' Кол-во мониторов {len(QtGui.QGuiApplication.screens())} \n'
                                           f' Текущий основной экран {QtGui.QGuiApplication.primaryScreen().name()}\n'
                                           f' Окно находится на {QtGui.QGuiApplication.screenAt(self.geometry().center()).name()} экране\n'
                                           f' Разрешение текущего экрана {QtGui.QGuiApplication.screenAt(self.geometry().center()).geometry().height()} х {QtGui.QGuiApplication.screenAt(self.geometry().center()).geometry().width()}\n'
                                           f' Размеры окна {self.size().height()} х {self.size().width()}\n'
                                           f' Минимальные размеры окна {self.minimumSize().height()} х {self.minimumSize().width()}\n'
                                           f' Текущее положение (координаты) окна x:{self.geometry().x()},y:{self.geometry().y()}\n'
                                           f' Координаты центра приложения x: {self.frameGeometry().center().x()} ,y: {self.frameGeometry().center().y()}\n'
                                           f' Cостояние окна {self.windowState().name}\n'
                                           )


    def onButtonMoveCoordsClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLineEdit

        :return: None
        """
        wx=self.geometry().x()
        wy = self.geometry().y()
        self.move(self.ui.spinBoxX.value(),self.ui.spinBoxY.value())
        self.peremesh(wx,wy,self.geometry().x(),self.geometry().y())
    def onPushButtonCenterClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLineEdit

        :return: None
        """
        wx=self.geometry().x()
        wy = self.geometry().y()
        qp = QtGui.QGuiApplication.screenAt(self.geometry().center()).geometry().center()
        self.move(qp.x()-self.size().width()/2,qp.y()-self.size().height()/2)
        self.peremesh(wx, wy, self.geometry().x(), self.geometry().y())
    def onPushButtonLTClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLineEdit

        :return: None
        """
        wx=self.geometry().x()
        wy = self.geometry().y()
        self.move(QtGui.QGuiApplication.screenAt(self.geometry().center()).geometry().topLeft())
        self.peremesh( wx, wy, self.geometry().x(), self.geometry().y())
    def onButtonRTClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLineEdit

        :return: None
        """
        wx=self.geometry().x()
        wy = self.geometry().y()
        qp=QtGui.QGuiApplication.screenAt(self.geometry().center()).geometry().topRight()
        self.move(qp.x()-self.size().width(),qp.y())
        self.peremesh( wx, wy, self.geometry().x(), self.geometry().y())
    def onPushButtonRBClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLineEdit

        :return: None
        """
        wx=self.geometry().x()
        wy = self.geometry().y()
        qp=QtGui.QGuiApplication.screenAt(self.geometry().center()).geometry().bottomRight()
        self.move(qp.x()-self.size().width(),qp.y()-self.size().height())
        self.peremesh( wx, wy, self.geometry().x(), self.geometry().y())
    def onPushButtonLBClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLineEdit

        :return: None
        """
        wx=self.geometry().x()
        wy = self.geometry().y()
        qp=QtGui.QGuiApplication.screenAt(self.geometry().center()).geometry().bottomLeft()
        self.move(qp.x(),qp.y()-self.size().height())
        self.peremesh( wx, wy, self.geometry().x(), self.geometry().y())
if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
