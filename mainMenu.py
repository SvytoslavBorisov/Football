import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainWindow import Ui_MainWindow
from gameWindow import Interface
from windowOfDataPlayers import BaseDataPlayers


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("#MainWindow {border-image: url(./images/mainWindow.jpg) 0 0 0 0 stretch stretch;"
                           "background-color : rgb(100, 130, 45);}")
        self.bExit.clicked.connect(self.exit)
        self.bNewGame.clicked.connect(self.newGame)
        self.bSettings.clicked.connect(self.baseDataPlayers)

    def exit(self):
        sys.exit(app.exec_())

    def newGame(self):
        self.exGame = Interface()
        self.exGame.showFullScreen()

    def baseDataPlayers(self):
        self.exData = BaseDataPlayers()
        self.exData.showFullScreen()


app = QApplication(sys.argv)
ex = MainWindow()
ex.showFullScreen()
sys.exit(app.exec_())