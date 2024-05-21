from PySide6 import QtWidgets
from PySide6 import QtGui
from PySide6 import QtCore
from ui.game_2048 import Ui_Game_2048
from ui.table_win import Ui_Form as table_win
import random as rand
import json
class dva_widgets(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.none_ind = ('00', '01', '02', '03', '10', '11', '12', '13', '20', '21', '22',
                    '23', '30', '31', '32', '33')
        self.painting_color={'2':'font: 700 20pt "Segoe UI";\nbackground-color: rgb(156, 0, 0);',
                             '4':'font: 700 20pt "Segoe UI";\nbackground-color: rgb(156, 156, 0);',
                             '8':'font: 700 20pt "Segoe UI";\nbackground-color: rgb(156, 0, 156);',
                             '16':'font: 700 20pt "Segoe UI";\nbackground-color: rgb(70, 0, 0);',
                             '32':'font: 700 20pt "Segoe UI";\nbackground-color: rgb(70, 70, 0);',
                             '64':'font: 700 20pt "Segoe UI";\nbackground-color: rgb(70, 0, 70);',
                             '128':'font: 700 20pt "Segoe UI";\nbackground-color: rgb(156, 156, 156);',
                             '256':'font: 700 20pt "Segoe UI";\nbackground-color: rgb(70, 70, 70);',
                             '512':'font: 700 20pt "Segoe UI";\nbackground-color: rgb(110, 0, 0);',
                             '1024':'font: 700 20pt "Segoe UI";\nbackground-color: rgb(0, 110, 0);',
                             '2048':'font: 700 20pt "Segoe UI";\nbackground-color: rgb(0, 0, 110);'}
        self.full_ind = {}
        self.int_list=None
        self.ui=Ui_Game_2048()
        self.ui.setupUi(self)
        self.list_lable=[[self.ui.label_00,self.ui.label_01,self.ui.label_02,self.ui.label_03],[self.ui.label_10,self.ui.label_11,self.ui.label_12,self.ui.label_13],[self.ui.label_20,self.ui.label_21,self.ui.label_22,self.ui.label_23],[self.ui.label_30,self.ui.label_31,self.ui.label_32,self.ui.label_33]]
        self.status=False
        self.config_settings = QtCore.QSettings("Game_2048")
        self.winners = json.loads(self.config_settings.value("winners", str('{}')))
        self._initsign()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Событие закрытия окна

        :param event: QtGui.QCloseEvent
        :return: None
        """

        # Сохранение списка IP-адресов в настройки
        self.config_settings.setValue(
            "winners", str(self.winners))

    def __new_elem(self):
        el = rand.choice([el for el in self.none_ind if el not in self.full_ind])
        self.full_ind[el]=1
        return int(el[0]),int(el[1])

    def you_win(self):
        if max(self.int_list) == 2048:
            QtWidgets.QMessageBox.warning(self, "Ахренеть", "Ты победил")
            self.status = False
            return
    def game_over(self):
        if len(self.full_ind) == len(self.none_ind):
            if self.proverka_ne_prosla():
                QtWidgets.QMessageBox.warning(self, "game_over", "Больше я тебе ходить не дам")
                self.status = False

    def repaint_kv(self):
        if len(self.full_ind) != len(self.none_ind):
            i, j = self.__new_elem()
            self.list_lable[i][j].setText(str(2))
            self.int_list[i][j] = 2
            self.paint_new()

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:

        if self.status:
            if event.key()==QtCore.Qt.Key_Up:
                self.need_up()
            if event.key()==QtCore.Qt.Key_Down:
                self.need_down()
            if event.key()==QtCore.Qt.Key_Left:
                self.need_left()
            if event.key()==QtCore.Qt.Key_Right:
                self.need_right()
            self.repaint_kv()
            self.you_win()
            self.game_over()

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.x_pos_was=event.globalPosition().x()
        self.y_pos_was = event.globalPosition().y()

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        self.x_pos_now=event.globalPosition().x()
        self.y_pos_now =event.globalPosition().y()

        if self.status and (self.x_pos_was!=self.x_pos_now or self.y_pos_was!=self.y_pos_now):
            if abs(self.x_pos_was-self.x_pos_now)>abs(self.y_pos_was-self.y_pos_now):
                if self.x_pos_was-self.x_pos_now>0:
                    self.need_left()
                else:
                    self.need_right()
            else:
                if self.y_pos_was - self.y_pos_now > 0:
                    self.need_up()
                else:
                    self.need_down()
            self.repaint_kv()
            self.you_win()
            self.game_over()

    def watch_winners(self):
        self.tablo=win_tablo()
        self.tablo.show()

    def need_up(self):
        self.count_new_V([0, 0, 0, 0], 1)
        self.recount_V([0, 1, 2], 1)
        self.count_new_V([0, 0, 0, 0], 1)
    def need_down(self):
        self.count_new_V([3, 3, 3, 3], -1)
        self.recount_V([3, 2, 1], -1)
        self.count_new_V([3, 3, 3, 3], -1)
    def need_left(self):
        self.count_new_H([0, 0, 0, 0], 1)
        self.recount_H([0, 1, 2], 1)
        self.count_new_H([0, 0, 0, 0], 1)
    def need_right(self):
        self.count_new_H([3, 3, 3, 3], -1)
        self.recount_H([3, 2, 1], -1)
        self.count_new_H([3, 3, 3, 3], -1)
    def start_restart_game(self):
        self.ui.start_pushButton.setText('Начать заново')
        self.status=True
        self.full_ind = {}
        self.int_list=[4 * [0],4 * [0],4 * [0],4 * [0]]
        for pow_ in range(3):
            i,j=self.__new_elem()
            self.list_lable[i][j].setText(str(2**(pow_+1)))
            self.int_list[i][j]=2**(pow_+1)
            self.paint_new()
        self.ui.label_3.setText(str(0))
        self.ui.groupBox.setFocus()

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
                    self.list_lable[i][j].setStyleSheet(self.painting_color[str(self.int_list[i][j])])
                else:
                    self.list_lable[i][j].setText('')
                    self.list_lable[i][j].setStyleSheet(u"font: 700 20pt \"Segoe UI\";")
    def recount_H(self,obl_ind, ind):
        for i in range(0,4):
            for j in obl_ind:
                if self.int_list[i][j] == self.int_list[i][j+ind] and self.int_list[i][j]!=0:
                    self.int_list[i][j]=self.int_list[i][j]*2
                    self.int_list[i][j+ind]=0
                    del self.full_ind[str(i)+str(j+ind)]
                    self.ui.label_3.setText(str(int(self.ui.label_3.text()) + self.int_list[i][j]))

    def recount_V(self,obl_ind, ind):
        for j in range(0,4):
            for i in obl_ind:
                if self.int_list[i][j] == self.int_list[i+ind][j] and self.int_list[i][j]!=0:
                    self.int_list[i][j]=self.int_list[i][j]*2
                    self.int_list[i+ind][j]=0
                    del self.full_ind[str(i+ind)+str(j)]
                    self.ui.label_3.setText(str(int(self.ui.label_3.text())+self.int_list[i][j]))

    def _initsign(self):
        self.ui.start_pushButton.clicked.connect(self.start_restart_game)
        self.ui.pushButton.clicked.connect(self.watch_winners)

    def proverka_ne_prosla(self):
            for i in range(0,4):
                for j in range(1,4):
                    if self.int_list[i][j]==self.int_list[i][j-1]:
                        return False
            for j in range(0,4):
                for i in range(1,4):
                    if self.int_list[i][j]==self.int_list[i-1][j]:
                        return False
            return True

class win_tablo(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui=table_win()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = dva_widgets()
    window.show()

    app.exec()