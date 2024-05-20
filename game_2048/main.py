from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6 import QtCore
from ui.game_2048 import Ui_Game_2048
import random as rand
class dva_widgets(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.none_ind = ('00', '01', '02', '03', '10', '11', '12', '13', '20', '21', '22',
                    '23', '30', '31', '32', '33')
        self.full_ind = {}
        # self.all_id = ['00', '01', '02', '03', '10', '11', '12', '13', '20', '21', '22',
        #             '23', '30', '31', '32', '33']
        # self.none_ind = {'00': 1, '01': 1, '02': 1, '03': 1, '10': 1, '11': 1, '12': 1, '13': 1, '20': 1, '21': 1, '22': 1,
        #             '23': 1, '30': 1, '31': 1, '32': 1, '33': 1}
        # self.full_ind = {'00': 0, '01': 0, '02': 0, '03': 0, '10': 0, '11': 0, '12': 0, '13': 0, '20': 0, '21': 0, '22': 0,
        #             '23': 0, '30': 0, '31': 0, '32': 0, '33': 0}
        self.int_list=[4*[0]]*4
        self.ui=Ui_Game_2048()
        self.ui.setupUi(self)
        self.list_lable=[[self.ui.label_00,self.ui.label_01,self.ui.label_02,self.ui.label_03],[self.ui.label_10,self.ui.label_11,self.ui.label_12,self.ui.label_13],[self.ui.label_20,self.ui.label_21,self.ui.label_22,self.ui.label_23],[self.ui.label_30,self.ui.label_31,self.ui.label_32,self.ui.label_33]]
        for pow_ in range(3):
            i,j=self.__new_elem()
            self.list_lable[i][j].setText(str(2**(pow_+1)))
            print(self.int_list[i])
            print(self.int_list[i][j])
            print(self.int_list)
            self.int_list[i][j]=2**(pow_+1)
            print(self.int_list[i])
            print(self.int_list[i][j])
            print(self.int_list)
    def __new_elem(self):
        el = rand.choice([el for el in self.none_ind if el not in self.full_ind])
        self.full_ind[el]=1
        return int(el[0]),int(el[1])

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:

        if event.key()==QtCore.Qt.Key_Up:
            pass
        if event.key()==QtCore.Qt.Key_Down:
            print('down')
        if event.key()==QtCore.Qt.Key_Left:
            self.count_new()
            self.paint_new()
        if event.key()==QtCore.Qt.Key_Right:
            print('right')

        # if len(self.none_ind)==0:
        #     print('game_over')
        # else:
        #     i, j = self.__new_elem()
        #     self.list_lable[i][j].setText(str(2))
        #     self.int_list[i][j] = 2

    def count_new(self):
        new_ris={}
        self.full_ind=sorted(self.full_ind)
        self.new_int_list = 4 * [4 * [0]]
        j=0
        i=-1
        for el in self.full_ind:
            if el[0]!=i:
                i=int(el[0])
                j=0
            self.new_int_list[i][j]=self.int_list[i][int(el[1])]
            new_ris[str(i)+str(j)]=1
            j=j+1
        self.full_ind=new_ris
        self.int_list=self.new_int_list
    def paint_new(self):
        for i in range(3):
            for j in range(3):
                if self.int_list[i][j]!=0:
                    self.list_lable[i][j].setText(str(self.int_list[i][j]))
                else:
                    self.list_lable[i][j].setText('')



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = dva_widgets()
    window.show()

    app.exec()