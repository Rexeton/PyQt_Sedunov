from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6 import QtCore
from ui.game_2048 import Ui_Game_2048
import random as rand
class dva_widgets(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.none_ind = {'00': 1, '01': 1, '02': 1, '03': 1, '10': 1, '11': 1, '12': 1, '13': 1, '20': 1, '21': 1, '22': 1,
                    '23': 1, '30': 1, '31': 1, '32': 1, '33': 1}
        self.full_ind = {'00': 0, '01': 0, '02': 0, '03': 0, '10': 0, '11': 0, '12': 0, '13': 0, '20': 0, '21': 0, '22': 0,
                    '23': 0, '30': 0, '31': 0, '32': 0, '33': 0}
        self.int_list=4*[4*[0]]
        self.ui=Ui_Game_2048()
        self.ui.setupUi(self)
        self.list_lable=[[self.ui.label_00,self.ui.label_01,self.ui.label_02,self.ui.label_03],[self.ui.label_10,self.ui.label_11,self.ui.label_12,self.ui.label_13],[self.ui.label_20,self.ui.label_21,self.ui.label_22,self.ui.label_23],[self.ui.label_30,self.ui.label_31,self.ui.label_32,self.ui.label_33]]
        for pow_ in range(3):
            i,j=self.__new_elem()
            self.list_lable[i][j].setText(str(2**(pow_+1)))
            self.int_list[i][j]=2**(pow_+1)
    def __new_elem(self):
        el = rand.choice([el for el in self.none_ind if self.none_ind[el] == 1])
        self.none_ind[el] -= 1
        self.full_ind[el] += 1
        return int(el[0]),int(el[1])

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key()==QtCore.Qt.Key_Up:
            print('up')
        if event.key()==QtCore.Qt.Key_Down:
            print('down')
        if event.key()==QtCore.Qt.Key_Left:
            print('left')
        if event.key()==QtCore.Qt.Key_Right:
            print('right')

        if len(self.none_ind)==0:
            print('game_over')
        else:
            i, j = self.__new_elem()
            self.list_lable[i][j].setText(str(2))
            self.int_list[i][j] = 2

    def paint_new(self,ind,jnd,pl):




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = dva_widgets()
    window.show()

    app.exec()