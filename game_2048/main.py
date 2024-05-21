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
        self.int_list=[4 * [0],4 * [0],4 * [0],4 * [0]]
        self.ui=Ui_Game_2048()
        self.ui.setupUi(self)
        self.list_lable=[[self.ui.label_00,self.ui.label_01,self.ui.label_02,self.ui.label_03],[self.ui.label_10,self.ui.label_11,self.ui.label_12,self.ui.label_13],[self.ui.label_20,self.ui.label_21,self.ui.label_22,self.ui.label_23],[self.ui.label_30,self.ui.label_31,self.ui.label_32,self.ui.label_33]]
        for pow_ in range(3):
            i,j=self.__new_elem()
            self.list_lable[i][j].setText(str(2**(pow_+1)))
            self.int_list[i][j]=2**(pow_+1)

    def __new_elem(self):
        el = rand.choice([el for el in self.none_ind if el not in self.full_ind])
        self.full_ind[el]=1
        return int(el[0]),int(el[1])

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if len(self.full_ind)==len(self.none_ind):
            print('game_over')
        else:
            if event.key()==QtCore.Qt.Key_Up:
                self.count_new_V([0,0,0,0],1)
                self.recount_V([0,1,2],1)
                self.count_new_V([0, 0, 0, 0], 1)
            if event.key()==QtCore.Qt.Key_Down:
                self.count_new_V([3,3,3,3],-1)
                self.recount_V([3, 2, 1], -1)
                self.count_new_V([3, 3, 3, 3], -1)
            if event.key()==QtCore.Qt.Key_Left:
                self.count_new_H([0,0,0,0],1)
                self.recount_H([0,1,2],1)
                self.count_new_H([0, 0, 0, 0], 1)
            if event.key()==QtCore.Qt.Key_Right:
                self.count_new_H([3,3,3,3],-1)
                self.recount_H([3, 2, 1], -1)
                self.count_new_H([3, 3, 3, 3], -1)
            self.paint_new()

            i, j = self.__new_elem()
            self.list_lable[i][j].setText(str(2))
            self.int_list[i][j] = 2

    def count_new_H(self,obl_ind,ind):
        new_ris={}
        self.full_ind=sorted(self.full_ind)[::ind]
        self.new_int_list =  [4 * [0],4 * [0],4 * [0],4 * [0]]
        for el in self.full_ind:
            i=int(el[0])
            j=obl_ind[i]
            self.new_int_list[i][j]=self.int_list[i][int(el[1])]
            new_ris[str(i)+str(j)]=1
            obl_ind[i]+=ind
        self.full_ind=new_ris
        self.int_list=self.new_int_list

    def count_new_V(self,obl_ind,ind):
        new_ris={}
        self.full_ind=sorted(self.full_ind)[::ind]
        self.new_int_list =  [4 * [0],4 * [0],4 * [0],4 * [0]]
        for el in self.full_ind:
            j = int(el[1])
            i=obl_ind[j]
            self.new_int_list[i][j]=self.int_list[int(el[0])][j]
            new_ris[str(i)+str(j)]=1
            obl_ind[j]+=ind
        self.full_ind=new_ris
        self.int_list=self.new_int_list

    def paint_new(self):
        for i in range(0,4):
            for j in range(0,4):
                if self.int_list[i][j]!=0:
                    self.list_lable[i][j].setText(str(self.int_list[i][j]))
                else:
                    self.list_lable[i][j].setText('')

    def recount_H(self,obl_ind, ind):
        for i in range(0,4):
            for j in obl_ind:
                if self.int_list[i][j] == self.int_list[i][j+ind] and self.int_list[i][j]!=0:
                    self.int_list[i][j]=self.int_list[i][j]*2
                    self.int_list[i][j+ind]=0
                    del self.full_ind[str(i)+str(j+ind)]

    def recount_V(self,obl_ind, ind):
        for j in range(0,4):
            for i in obl_ind:
                if self.int_list[i][j] == self.int_list[i+ind][j] and self.int_list[i][j]!=0:
                    self.int_list[i][j]=self.int_list[i][j]*2
                    self.int_list[i+ind][j]=0
                    del self.full_ind[str(i+ind)+str(j)]

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = dva_widgets()
    window.show()

    app.exec()