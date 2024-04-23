from PySide6 import QtWidgets
from ui.login import Ui_Form
DEBUG=True
class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        if DEBUG:
            self.ui.login.setPlaceholderText('Vvedite_login')
            self.ui.password.setPlaceholderText('Vvedite_parol')


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()