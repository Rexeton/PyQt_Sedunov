from PySide6 import QtWidgets
from ui.book_shop import Ui_Form as book_shop
class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = book_shop()
        self.ui.setupUi(self)
