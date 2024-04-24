from PySide6 import QtWidgets
from ui.role_aircraft import Ui_Form as role_aircraft
class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = role_aircraft()
        self.ui.setupUi(self)

