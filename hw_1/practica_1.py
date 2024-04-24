from PySide6 import QtWidgets

from g_calculator import Window as Calc_form
from f_book_shop import Window as Book_shop_form
from c_ship_parameters import Window as Sheep_parametr_form
from d_engine_settings import Window as Role_aircraft_form
from b_login import Window as Login_form
from e_profile_card import Window as Prof_card

DEBUG=True
class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.CalcWidget = Calc_form()
        self.LoginWidget = Login_form()
        self.ShipParametersWidget = Sheep_parametr_form()
        self.EngineSettingsWidget = Role_aircraft_form()
        self.Book_shopWidget = Book_shop_form()
        self.ProfileCardWidget = Prof_card()

        l_first = QtWidgets.QVBoxLayout()
        l_first.addWidget(self.CalcWidget)
        l_first.addWidget(self.ProfileCardWidget)
        l_first.addWidget(self.ShipParametersWidget)
        # l_first.addSpacerItem(QtWidgets.QSpacerItem(
        #     0, 10, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding
        # ))
        l_second= QtWidgets.QVBoxLayout()

        l_second.addWidget(self.LoginWidget)
        l_second.addWidget(self.Book_shopWidget)
        l_second.addSpacerItem(QtWidgets.QSpacerItem(
            0, 10, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding
        ))

        l_top = QtWidgets.QHBoxLayout()
        l_top.addLayout(l_first)
        l_top.addLayout(l_second)

        l_main = QtWidgets.QVBoxLayout()
        l_main.addLayout(l_top)
        l_main.addWidget(self.EngineSettingsWidget)

        self.setLayout(l_main)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
