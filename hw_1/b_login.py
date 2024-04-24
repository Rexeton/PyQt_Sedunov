from PySide6 import QtWidgets
from ui.login import Ui_Form as login
class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = login()
        self.ui.setupUi(self)

