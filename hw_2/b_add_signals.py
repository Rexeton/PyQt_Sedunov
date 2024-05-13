import random

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()# TODO: Вызвать метод с инициализацией сигналов

    def initUi(self) -> None:
        """
        Инициализация интерфейса

        :return: None
        """

        # comboBox -----------------------------------------------------------
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItem("Элемент 1")
        self.comboBox.addItem("Элемент 2")
        self.comboBox.addItems(["Элемент 3", "Элемент 4", "Элемент 5"])
        self.comboBox.insertItem(0, "")

        self.pushButtonComboBox = QtWidgets.QPushButton("Получить данные")

        layoutComboBox = QtWidgets.QHBoxLayout()
        layoutComboBox.addWidget(self.comboBox)
        layoutComboBox.addWidget(self.pushButtonComboBox)

        # lineEdit -----------------------------------------------------------
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setPlaceholderText("Введите текст")

        self.pushButtonLineEdit = QtWidgets.QPushButton("Получить данные")

        layoutLineEdit = QtWidgets.QHBoxLayout()
        layoutLineEdit.addWidget(self.lineEdit)
        layoutLineEdit.addWidget(self.pushButtonLineEdit)

        # textEdit -----------------------------------------------------------
        self.textEdit = QtWidgets.QTextEdit()
        self.textEdit.setPlaceholderText("Введите текст")

        self.pushButtonTextEdit = QtWidgets.QPushButton("Получить данные")

        layoutTextEdit = QtWidgets.QHBoxLayout()
        layoutTextEdit.addWidget(self.textEdit)
        layoutTextEdit.addWidget(self.pushButtonTextEdit)

        # plainTextEdit ------------------------------------------------------
        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setPlaceholderText("Введите текст")

        self.pushButtonPlainTextEdit = QtWidgets.QPushButton("Получить данные")

        layoutPlainTextEdit = QtWidgets.QHBoxLayout()
        layoutPlainTextEdit.addWidget(self.plainTextEdit)
        layoutPlainTextEdit.addWidget(self.pushButtonPlainTextEdit)

        # spinBox ------------------------------------------------------------
        self.spinBox = QtWidgets.QSpinBox()
        self.spinBox.setValue(random.randint(-50, 50))

        self.pushButtonSpinBox = QtWidgets.QPushButton("Получить данные")

        layoutSpinBox = QtWidgets.QHBoxLayout()
        layoutSpinBox.addWidget(self.spinBox)
        layoutSpinBox.addWidget(self.pushButtonSpinBox)

        # doubleSpinBox ------------------------------------------------------
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox()
        self.doubleSpinBox.setValue(random.randint(-50, 50))

        self.pushButtonDoubleSpinBox = QtWidgets.QPushButton("Получить данные")

        layoutDoubleSpinBox = QtWidgets.QHBoxLayout()
        layoutDoubleSpinBox.addWidget(self.doubleSpinBox)
        layoutDoubleSpinBox.addWidget(self.pushButtonDoubleSpinBox)

        # timeEdit -----------------------------------------------------------
        self.timeEdit = QtWidgets.QTimeEdit()
        self.timeEdit.setTime(QtCore.QTime.currentTime().addSecs(random.randint(-10000, 10000)))

        self.pushButtonTimeEdit = QtWidgets.QPushButton("Получить данные")

        layoutTimeEdit = QtWidgets.QHBoxLayout()
        layoutTimeEdit.addWidget(self.timeEdit)
        layoutTimeEdit.addWidget(self.pushButtonTimeEdit)

        # dateTimeEdit -------------------------------------------------------
        self.dateTimeEdit = QtWidgets.QDateTimeEdit()
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime().addDays(random.randint(-10, 10)))

        self.pushButtonDateTimeEdit = QtWidgets.QPushButton("Получить данные")

        layoutDateTimeEdit = QtWidgets.QHBoxLayout()
        layoutDateTimeEdit.addWidget(self.dateTimeEdit)
        layoutDateTimeEdit.addWidget(self.pushButtonDateTimeEdit)

        # plainTextEditLog ---------------------------------------------------
        self.plainTextEditLog = QtWidgets.QPlainTextEdit()

        self.pushButtonClearLog = QtWidgets.QPushButton("Очистить лог")

        layoutLog = QtWidgets.QHBoxLayout()
        layoutLog.addWidget(self.plainTextEditLog)
        layoutLog.addWidget(self.pushButtonClearLog)

        # main layout

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutComboBox)
        layoutMain.addLayout(layoutLineEdit)
        layoutMain.addLayout(layoutTextEdit)
        layoutMain.addLayout(layoutPlainTextEdit)
        layoutMain.addLayout(layoutSpinBox)
        layoutMain.addLayout(layoutDoubleSpinBox)
        layoutMain.addLayout(layoutTimeEdit)
        layoutMain.addLayout(layoutDateTimeEdit)
        layoutMain.addLayout(layoutLog)

        self.setLayout(layoutMain)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButtonComboBox.clicked.connect(self.onPushButtonComboBoxClicked)  # TODO подключить слот для вывода текста из comboBox в plainTextEditLog при нажатии на кнопку
        self.pushButtonLineEdit.clicked.connect(self.onPushButtonLineEditClicked)
        self.pushButtonTextEdit.clicked.connect(self.onPushButtonTextEditClicked)  # TODO подключить слот для вывода текста из textEdit в plainTextEditLog при нажатии на кнопку
        self.pushButtonPlainTextEdit.clicked.connect(self.onPushButtonPlainTextClicked)   # TODO подключить слот для вывода текста из plaineTextEdit в plainTextEditLog при нажатии на кнопку
        self.pushButtonSpinBox.clicked.connect(self.onPushButtonSpinBoxClicked)  # TODO подключить слот для вывода значения из spinBox в plainTextEditLog при нажатии на кнопку
        self.pushButtonDoubleSpinBox.clicked.connect(self.onPushButtondoubleSpinBoxClicked) # TODO подключить слот для вывода значения из doubleSpinBox в plainTextEditLog при нажатии на кнопку
        self.pushButtonTimeEdit.clicked.connect(self.onPushButtontimeEditClicked)  # TODO подключить слот для вывода времени из timeEdit в plainTextEditLog при нажатии на кнопку
        self.pushButtonDateTimeEdit.clicked.connect(self.onPushButtonDateTimeClicked)  # TODO подключить слот для вывода времени из dateTimeEdit в plainTextEditLog при нажатии на кнопку
        self.pushButtonClearLog.clicked.connect(self.onPushButtonClearLogClicked)  # TODO подключить слот для очистки plainTextEditLog при нажатии на кнопку

        self.comboBox.currentTextChanged.connect(self.onPushButtonComboBoxClicked)  # TODO подключить слот для вывода текста в plainTextEditLog при изменении выбранного элемента в comboBox
        self.spinBox.valueChanged.connect(self.onPushButtonSpinBoxClicked)  # TODO подключить слот для вывода значения в plainTextEditLog при изменении значения в spinBox
        self.dateTimeEdit.dateTimeChanged.connect(self.onPushButtonDateTimeClicked)  # TODO подключить слот для вывода датывремени в plainTextEditLog при изменении датывремени в dateTimeEdit

    # slots --------------------------------------------------------------
    def onPushButtonLineEditClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLineEdit

        :return: None
        """

        self.plainTextEditLog.setPlainText(self.lineEdit.text())

    def onPushButtonComboBoxClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonComboBox

        :return: None
        """

        self.plainTextEditLog.setPlainText(self.comboBox.currentText())

    def onPushButtonTextEditClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonTextEdit

        :return: None
        """
        self.plainTextEditLog.setPlainText(self.textEdit.toPlainText())

    def onPushButtonPlainTextClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonPlainText

        :return: None
        """
        self.plainTextEditLog.setPlainText(self.plainTextEdit.toPlainText())

    def onPushButtonSpinBoxClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonSpinBox

        :return: None
        """
        self.plainTextEditLog.setPlainText(str(self.spinBox.value()))

    def onPushButtondoubleSpinBoxClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushdoubleSpinBox

        :return: None
        """
        self.plainTextEditLog.setPlainText(str(self.doubleSpinBox.value()))

    def onPushButtontimeEditClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushtimeEdit

        :return: None
        """
        h=self.timeEdit.time().hour()
        m=self.timeEdit.time().minute()
        self.plainTextEditLog.setPlainText(self.timeEdit.time().toString())

    def onPushButtonDateTimeClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushDateTime

        :return: None
        """

        self.plainTextEditLog.setPlainText(self.dateTimeEdit.dateTime().toString())

    def onPushButtonClearLogClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushClearLog

        :return: None
        """
        self.plainTextEditLog.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
