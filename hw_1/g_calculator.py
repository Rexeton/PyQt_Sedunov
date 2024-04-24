from PySide6 import QtWidgets
from ui.calc import Ui_Form as Calc_form
class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Calc_form()
        self.ui.setupUi(self)

