from PySide6 import QtWidgets
from ui.prof_card import Ui_Form as prof_card
class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = prof_card()
        self.ui.setupUi(self)

