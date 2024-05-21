# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_2048.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Game_2048(object):
    def setupUi(self, Game_2048):
        if not Game_2048.objectName():
            Game_2048.setObjectName(u"Game_2048")
        Game_2048.resize(768, 804)
        self.verticalLayout_5 = QVBoxLayout(Game_2048)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_2 = QGroupBox(Game_2048)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 70))
        self.groupBox_2.setMaximumSize(QSize(16777215, 130))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(130, 0))
        self.groupBox_4.setStyleSheet(u"background-color: rgb(255, 255, 190);")
        self.groupBox_4.setFlat(True)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_3)


        self.horizontalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(130, 100))
        font = QFont()
        font.setPointSize(9)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAutoFillBackground(False)
        self.groupBox_3.setStyleSheet(u"background-color: rgb(255, 255, 190);")
        self.groupBox_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox_3.setFlat(True)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_4)


        self.horizontalLayout_2.addWidget(self.groupBox_3)

        self.horizontalSpacer = QSpacerItem(293, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 100))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 190);")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.start_pushButton = QPushButton(self.groupBox_2)
        self.start_pushButton.setObjectName(u"start_pushButton")
        self.start_pushButton.setMinimumSize(QSize(0, 100))
        self.start_pushButton.setStyleSheet(u"background-color: rgb(255, 255, 190);")

        self.horizontalLayout_2.addWidget(self.start_pushButton)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(Game_2048)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"background-color: rgb(255, 255, 190);")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_00 = QLabel(self.groupBox)
        self.label_00.setObjectName(u"label_00")
        self.label_00.setStyleSheet(u"font: 700 20pt \"Segoe UI\";")
        self.label_00.setFrameShape(QFrame.Shape.Box)
        self.label_00.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_00)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 700 20pt \"Segoe UI\";")
        self.label_10.setFrameShape(QFrame.Shape.Box)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_10)

        self.label_20 = QLabel(self.groupBox)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"font: 700 20pt \"Segoe UI\";")
        self.label_20.setFrameShape(QFrame.Shape.Box)
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_20)

        self.label_30 = QLabel(self.groupBox)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"font: 700 20pt \"Segoe UI\";")
        self.label_30.setFrameShape(QFrame.Shape.Box)
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_30)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_01 = QLabel(self.groupBox)
        self.label_01.setObjectName(u"label_01")
        self.label_01.setStyleSheet(u"font: 700 20pt \"Segoe UI\";")
        self.label_01.setFrameShape(QFrame.Shape.Box)
        self.label_01.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_01)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 700 20pt \"Segoe UI\";")
        self.label_11.setFrameShape(QFrame.Shape.Box)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_11)

        self.label_21 = QLabel(self.groupBox)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font: 700 20pt \"Segoe UI\";")
        self.label_21.setFrameShape(QFrame.Shape.Box)
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_21)

        self.label_31 = QLabel(self.groupBox)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"font: 700 20pt \"Segoe UI\";")
        self.label_31.setFrameShape(QFrame.Shape.Box)
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_31)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_02 = QLabel(self.groupBox)
        self.label_02.setObjectName(u"label_02")
        self.label_02.setStyleSheet(u"font: 700 20pt \"Segoe UI\";")
        self.label_02.setFrameShape(QFrame.Shape.Box)
        self.label_02.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_02)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font: 700 20pt \"Segoe UI\";")
        self.label_12.setFrameShape(QFrame.Shape.Box)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_12)

        self.label_22 = QLabel(self.groupBox)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"font: 700 20pt \"Segoe UI\";")
        self.label_22.setFrameShape(QFrame.Shape.Box)
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_22)

        self.label_32 = QLabel(self.groupBox)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"font: 700 20pt \"Segoe UI\";")
        self.label_32.setFrameShape(QFrame.Shape.Box)
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_32)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_03 = QLabel(self.groupBox)
        self.label_03.setObjectName(u"label_03")
        self.label_03.setStyleSheet(u"font: 700 20pt \"Segoe UI\";")
        self.label_03.setFrameShape(QFrame.Shape.Box)
        self.label_03.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_03.setMargin(1)

        self.verticalLayout_3.addWidget(self.label_03)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 700 20pt \"Segoe UI\";")
        self.label_13.setFrameShape(QFrame.Shape.Box)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_13)

        self.label_23 = QLabel(self.groupBox)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font: 700 20pt \"Segoe UI\";")
        self.label_23.setFrameShape(QFrame.Shape.Box)
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_23)

        self.label_33 = QLabel(self.groupBox)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"font: 700 20pt \"Segoe UI\";")
        self.label_33.setFrameShape(QFrame.Shape.Box)
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_33)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addWidget(self.groupBox)


        self.retranslateUi(Game_2048)

        QMetaObject.connectSlotsByName(Game_2048)
    # setupUi

    def retranslateUi(self, Game_2048):
        Game_2048.setWindowTitle(QCoreApplication.translate("Game_2048", u"2048", None))
        self.groupBox_2.setTitle("")
        self.groupBox_4.setTitle("")
        self.label.setText(QCoreApplication.translate("Game_2048", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.label_3.setText(QCoreApplication.translate("Game_2048", u"0", None))
        self.groupBox_3.setTitle("")
        self.label_2.setText(QCoreApplication.translate("Game_2048", u"\u0420\u0435\u043a\u043e\u0440\u0434", None))
        self.label_4.setText(QCoreApplication.translate("Game_2048", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("Game_2048", u"\u041f\u043e\u0431\u0435\u0434\u0438\u0442\u0435\u043b\u0438", None))
        self.start_pushButton.setText(QCoreApplication.translate("Game_2048", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0438\u0433\u0440\u0443", None))
        self.groupBox.setTitle("")
        self.label_00.setText("")
        self.label_10.setText("")
        self.label_20.setText("")
        self.label_30.setText("")
        self.label_01.setText("")
        self.label_11.setText("")
        self.label_21.setText("")
        self.label_31.setText("")
        self.label_02.setText("")
        self.label_12.setText("")
        self.label_22.setText("")
        self.label_32.setText("")
        self.label_03.setText("")
        self.label_13.setText("")
        self.label_23.setText("")
        self.label_33.setText("")
    # retranslateUi

