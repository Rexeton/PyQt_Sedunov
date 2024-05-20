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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Game_2048(object):
    def setupUi(self, Game_2048):
        if not Game_2048.objectName():
            Game_2048.setObjectName(u"Game_2048")
        Game_2048.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(Game_2048)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_00 = QLabel(Game_2048)
        self.label_00.setObjectName(u"label_00")
        self.label_00.setFrameShape(QFrame.Shape.Box)
        self.label_00.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_00)

        self.label_10 = QLabel(Game_2048)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFrameShape(QFrame.Shape.Box)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_10)

        self.label_20 = QLabel(Game_2048)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFrameShape(QFrame.Shape.Box)
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_20)

        self.label_30 = QLabel(Game_2048)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFrameShape(QFrame.Shape.Box)
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_30)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_01 = QLabel(Game_2048)
        self.label_01.setObjectName(u"label_01")
        self.label_01.setFrameShape(QFrame.Shape.Box)
        self.label_01.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_01)

        self.label_11 = QLabel(Game_2048)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFrameShape(QFrame.Shape.Box)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_11)

        self.label_21 = QLabel(Game_2048)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFrameShape(QFrame.Shape.Box)
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_21)

        self.label_31 = QLabel(Game_2048)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFrameShape(QFrame.Shape.Box)
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_31)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_02 = QLabel(Game_2048)
        self.label_02.setObjectName(u"label_02")
        self.label_02.setFrameShape(QFrame.Shape.Box)
        self.label_02.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_02)

        self.label_12 = QLabel(Game_2048)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFrameShape(QFrame.Shape.Box)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_12)

        self.label_22 = QLabel(Game_2048)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFrameShape(QFrame.Shape.Box)
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_22)

        self.label_32 = QLabel(Game_2048)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFrameShape(QFrame.Shape.Box)
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_32)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_03 = QLabel(Game_2048)
        self.label_03.setObjectName(u"label_03")
        self.label_03.setFrameShape(QFrame.Shape.Box)
        self.label_03.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_03)

        self.label_13 = QLabel(Game_2048)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFrameShape(QFrame.Shape.Box)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_13)

        self.label_23 = QLabel(Game_2048)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFrameShape(QFrame.Shape.Box)
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_23)

        self.label_33 = QLabel(Game_2048)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFrameShape(QFrame.Shape.Box)
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_33)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.retranslateUi(Game_2048)

        QMetaObject.connectSlotsByName(Game_2048)
    # setupUi

    def retranslateUi(self, Game_2048):
        Game_2048.setWindowTitle(QCoreApplication.translate("Game_2048", u"2048", None))
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

