# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(587, 481)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, -60, 531, 481))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bSettings = QtWidgets.QPushButton(self.frame)
        self.bSettings.setGeometry(QtCore.QRect(10, 160, 511, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.bSettings.setFont(font)
        self.bSettings.setStyleSheet("QPushButton\n"
"{\n"
"background-color:qlineargradient(spread:reflect, x1:0.493955, y1:0.051, x2:0.5, y2:0.528318, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(100, 100, 100, 255));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:qlineargradient(spread:reflect, x1:0.493955, y1:0.051, x2:0.5, y2:0.528318, stop:0 rgba(100, 100, 100, 255), stop:1 rgba(100, 100, 100, 255));\n"
"border-style:inset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:qlineargradient(spread:reflect, x1:0.493955, y1:0.051, x2:0.5, y2:0.528318, stop:0 rgba(100, 100, 100, 255), stop:1 rgba(180, 180, 180, 255));\n"
"border-style:inset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"}")
        self.bSettings.setFlat(False)
        self.bSettings.setObjectName("bSettings")
        self.bExit = QtWidgets.QPushButton(self.frame)
        self.bExit.setGeometry(QtCore.QRect(10, 240, 511, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.bExit.setFont(font)
        self.bExit.setStyleSheet("QPushButton\n"
"{\n"
"background-color:qlineargradient(spread:reflect, x1:0.493955, y1:0.051, x2:0.5, y2:0.528318, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(100, 100, 100, 255));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:qlineargradient(spread:reflect, x1:0.493955, y1:0.051, x2:0.5, y2:0.528318, stop:0 rgba(100, 100, 100, 255), stop:1 rgba(100, 100, 100, 255));\n"
"border-style:inset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:qlineargradient(spread:reflect, x1:0.493955, y1:0.051, x2:0.5, y2:0.528318, stop:0 rgba(100, 100, 100, 255), stop:1 rgba(180, 180, 180, 255));\n"
"border-style:inset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"}")
        self.bExit.setFlat(False)
        self.bExit.setObjectName("bExit")
        self.bNewGame = QtWidgets.QPushButton(self.frame)
        self.bNewGame.setGeometry(QtCore.QRect(10, 80, 511, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.bNewGame.setFont(font)
        self.bNewGame.setStyleSheet("QPushButton\n"
"{\n"
"background-color:qlineargradient(spread:reflect, x1:0.493955, y1:0.051, x2:0.5, y2:0.528318, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(100, 100, 100, 255));\n"
"color:white;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:qlineargradient(spread:reflect, x1:0.493955, y1:0.051, x2:0.5, y2:0.528318, stop:0 rgba(100, 100, 100, 255), stop:1 rgba(100, 100, 100, 255));\n"
"border-style:inset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:qlineargradient(spread:reflect, x1:0.493955, y1:0.051, x2:0.5, y2:0.528318, stop:0 rgba(100, 100, 100, 255), stop:1 rgba(180, 180, 180, 255));\n"
"border-style:inset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"}")
        self.bNewGame.setDefault(False)
        self.bNewGame.setFlat(False)
        self.bNewGame.setObjectName("bNewGame")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 587, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bSettings.setText(_translate("MainWindow", "База данных"))
        self.bExit.setText(_translate("MainWindow", "Выйти из игры"))
        self.bNewGame.setText(_translate("MainWindow", "Новая игра"))
