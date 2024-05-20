"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""

from PySide6 import QtWidgets
import b_systeminfo_widget,c_weatherapi_widget

class all_widgets(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.CPURAMWidget = b_systeminfo_widget.Sys_inf()
        self.WeaterWidget = c_weatherapi_widget.weth_inf()
        l_main = QtWidgets.QVBoxLayout()
        l_main.addWidget(self.CPURAMWidget)
        l_main.addWidget(self.WeaterWidget)
        self.setLayout(l_main)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = all_widgets()
    window.show()

    app.exec()