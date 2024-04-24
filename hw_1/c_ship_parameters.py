from PySide6 import QtWidgets
from ui.sheep_parametr import Ui_Form as sheep_parametr
class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = sheep_parametr()
        self.ui.setupUi(self)

