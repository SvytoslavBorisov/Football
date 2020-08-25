import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from gameSostavUI import Ui_MainWindow
from PyQt5.QtCore import Qt


class gameSostav(QMainWindow, Ui_MainWindow):
    def __init__(self, temp):
        super().__init__()
        self.setupUi(self)
        self.lTeam1.setText(temp.teams[0].name)
        self.lTeam2.setText(temp.teams[1].name)
        self.lScore.setText(temp.returnResult())
        for x in temp.structures[0]:
            if not [0, x] in temp.whoScoreHome:
                self.lwTeam1.addItem(temp.teams[0].players[x].name)
            else:
                self.lwTeam1.addItem(temp.teams[0].players[x].name)
        for x in temp.structures[1]:
            if not [1, x] in temp.whoScoreGuest:
                self.lwTeam2.addItem(temp.teams[1].players[x].name)
            else:
                self.lwTeam2.addItem(temp.teams[1].players[x].name)
        for x in temp.history:
            self.lwMatch.addItem(x)
        index = 0
        flg = True
        self.lwMainHistory.addItem('1 ТАЙМ')
        self.lwMainHistory.item(index).setTextAlignment(Qt.AlignCenter)
        for x in temp.mainHistory:
            index += 1
            if x[2] > 270 and flg:
                self.lwMainHistory.addItem('2 ТАЙМ')
                self.lwMainHistory.item(index).setTextAlignment(Qt.AlignCenter)
                index += 1
                flg = False
            if x[1] == 0:
                self.lwMainHistory.addItem(str(x[2] // 6 + 1) + '` ' + x[0])
            else:
                self.lwMainHistory.addItem(x[0] + ' ' + str(x[2] // 6 + 1) + '`')
                self.lwMainHistory.item(index).setTextAlignment(Qt.AlignRight)
        index += 1
        if flg:
            self.lwMainHistory.addItem('2 ТАЙМ')
            self.lwMainHistory.item(index).setTextAlignment(Qt.AlignCenter)