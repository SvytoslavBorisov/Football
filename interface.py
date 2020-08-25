# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(779, 618)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setTabletTracking(False)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon.fromTheme("FM2018")
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color : (0, 0,  0);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tv = QtWidgets.QTabWidget(self.centralwidget)
        self.tv.setObjectName("tv")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.tableViewForTeams = QtWidgets.QTableView(self.tab)
        self.tableViewForTeams.setStyleSheet("QHeaderView {\n"
"    font-size : 16 px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"     background-color: qlineargradient(x1:0, y1:0, x2:0, y2:0,\n"
"                                       stop:0 #616161, stop: 0.5 #505050,\n"
"                                       stop: 0.6 #434343, stop:1 #656565);\n"
"     color: white;\n"
"     padding-left: 4px;\n"
"     border: 1px solid #6c6c6c;\n"
" }")
        self.tableViewForTeams.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableViewForTeams.setLineWidth(1)
        self.tableViewForTeams.setSortingEnabled(False)
        self.tableViewForTeams.setObjectName("tableViewForTeams")
        self.tableViewForTeams.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableViewForTeams, 0, 0, 1, 1)
        self.tv.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableViewForPlayers = QtWidgets.QTableView(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableViewForPlayers.sizePolicy().hasHeightForWidth())
        self.tableViewForPlayers.setSizePolicy(sizePolicy)
        self.tableViewForPlayers.setAcceptDrops(True)
        self.tableViewForPlayers.setToolTipDuration(-1)
        self.tableViewForPlayers.setStyleSheet("QHeaderView {\n"
"    font-size : 16 px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"     background-color: qlineargradient(x1:0, y1:0, x2:0, y2:0,\n"
"                                       stop:0 #616161, stop: 0.5 #505050,\n"
"                                       stop: 0.6 #434343, stop:1 #656565);\n"
"     color: white;\n"
"     padding-left: 4px;\n"
"     border: 1px solid #6c6c6c;\n"
" }")
        self.tableViewForPlayers.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableViewForPlayers.setObjectName("tableViewForPlayers")
        self.tableViewForPlayers.verticalHeader().setVisible(False)
        self.verticalLayout_4.addWidget(self.tableViewForPlayers)
        self.tv.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableViewForPlayersPass = QtWidgets.QTableView(self.tab_3)
        self.tableViewForPlayersPass.setStyleSheet("QHeaderView {\n"
"    font-size : 16 px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"     background-color: qlineargradient(x1:0, y1:0, x2:0, y2:0,\n"
"                                       stop:0 #616161, stop: 0.5 #505050,\n"
"                                       stop: 0.6 #434343, stop:1 #656565);\n"
"     color: white;\n"
"     padding-left: 4px;\n"
"     border: 1px solid #6c6c6c;\n"
" }")
        self.tableViewForPlayersPass.setObjectName("tableViewForPlayersPass")
        self.tableViewForPlayersPass.verticalHeader().setVisible(False)
        self.verticalLayout_5.addWidget(self.tableViewForPlayersPass)
        self.tv.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tvSelection = QtWidgets.QTableView(self.tab_5)
        self.tvSelection.setStyleSheet("QHeaderView {\n"
"    font-size : 16 px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"     background-color: qlineargradient(x1:0, y1:0, x2:0, y2:0,\n"
"                                       stop:0 #616161, stop: 0.5 #505050,\n"
"                                       stop: 0.6 #434343, stop:1 #656565);\n"
"     color: white;\n"
"     padding-left: 4px;\n"
"     border: 1px solid #6c6c6c;\n"
" }")
        self.tvSelection.setObjectName("tvSelection")
        self.tvSelection.verticalHeader().setVisible(False)
        self.tvSelection.verticalHeader().setHighlightSections(False)
        self.horizontalLayout_3.addWidget(self.tvSelection)
        self.tv.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tvGoalKeapers = QtWidgets.QTableView(self.tab_6)
        self.tvGoalKeapers.setStyleSheet("QHeaderView {\n"
"    font-size : 16 px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"     background-color: qlineargradient(x1:0, y1:0, x2:0, y2:0,\n"
"                                       stop:0 #616161, stop: 0.5 #505050,\n"
"                                       stop: 0.6 #434343, stop:1 #656565);\n"
"     color: white;\n"
"     padding-left: 4px;\n"
"     border: 1px solid #6c6c6c;\n"
" }")
        self.tvGoalKeapers.setObjectName("tvGoalKeapers")
        self.tvGoalKeapers.verticalHeader().setVisible(False)
        self.tvGoalKeapers.verticalHeader().setHighlightSections(False)
        self.verticalLayout_7.addWidget(self.tvGoalKeapers)
        self.tv.addTab(self.tab_6, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.listView = QtWidgets.QListView(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(14)
        self.listView.setFont(font)
        self.listView.setStyleSheet("QListView::item:alternate {\n"
"    background: #EEEEEE;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border: 1px solid #6a6ea9;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #ABAFE5, stop: 1 #8588B2);\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #FAFBFE, stop: 1 #DCDEF1);\n"
"}")
        self.listView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listView.setTextElideMode(QtCore.Qt.ElideLeft)
        self.listView.setObjectName("listView")
        self.verticalLayout_6.addWidget(self.listView)
        self.tv.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tv)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.bNextTour = QtWidgets.QPushButton(self.centralwidget)
        self.bNextTour.setAutoFillBackground(False)
        self.bNextTour.setStyleSheet("QPushButton\n"
"{\n"
"background-color:qlineargradient(spread:reflect, x1:0.493955, y1:0.051, x2:0.5, y2:0.528318, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(170, 255, 255, 255));\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: gray;\n"
"min-width: 6em;\n"
"padding: 6px;\n"
"}\n"
"QPushButton:hover \n"
"{ \n"
"background-color:qlineargradient(spread:reflect, x1:0.493955, y1:0.051, x2:0.5, y2:0.528318, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(170, 255, 255, 255));\n"
"border-style:inset; \n"
"border-width: 1px; \n"
"border-radius: 10px; \n"
"border-color: beige;\n"
"font: bold;\n"
"min-width: 6em;\n"
"padding: 6px; \n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:qlineargradient(spread:reflect, x1:0.493955, y1:0.051, x2:0.5, y2:0.528318, stop:0 rgba(180, 255, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
"border-style:inset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: gray;\n"
"min-width: 6em;\n"
"padding: 6px;\n"
"}")
        self.bNextTour.setObjectName("bNextTour")
        self.verticalLayout_2.addWidget(self.bNextTour)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.bExit = QtWidgets.QPushButton(self.centralwidget)
        self.bExit.setStyleSheet("QPushButton\n"
"{\n"
"background-color:qlineargradient(spread:reflect, x1:0.493955, y1:0.051, x2:0.5, y2:0.528318, \n"
"stop:0 rgba(255, 80, 0, 255), stop:1 rgba(255, 180, 30, 255));\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: gray;\n"
"min-width: 6em;\n"
"padding: 6px;\n"
"}\n"
"QPushButton:hover \n"
"{ \n"
"background-color:qlineargradient(spread:reflect, x1:0.493955, y1:0.051, x2:0.5, y2:0.528318, \n"
"stop:0 rgba(255, 80, 0, 255), stop:1 rgba(255, 180, 30, 255));\n"
"border-style:inset; \n"
"border-width: 1px; \n"
"border-radius: 10px; \n"
"border-color: beige;\n"
"font: bold;\n"
"min-width: 6em;\n"
"padding: 6px; \n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:qlineargradient(spread:reflect, x1:0.493955, y1:0.051, x2:0.5, y2:0.528318, \n"
"stop:0 rgba(255,1 80, 0, 255), stop:1 rgba(255, 0, 30, 255));\n"
"border-style:inset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: gray;\n"
"min-width: 6em;\n"
"padding: 6px;\n"
"}")
        self.bExit.setObjectName("bExit")
        self.verticalLayout_2.addWidget(self.bExit)
        self.verticalLayout_2.setStretch(1, 10)
        self.verticalLayout_2.setStretch(2, 5)
        self.verticalLayout_2.setStretch(3, 5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tv.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Футбольный менеджер 2018"))
        self.tv.setTabText(self.tv.indexOf(self.tab), _translate("MainWindow", "Таблица"))
        self.tv.setTabText(self.tv.indexOf(self.tab_2), _translate("MainWindow", "Бомбардирды"))
        self.tv.setTabText(self.tv.indexOf(self.tab_3), _translate("MainWindow", "Распасовщики"))
        self.tv.setTabText(self.tv.indexOf(self.tab_5), _translate("MainWindow", "Перехватчики"))
        self.tv.setTabText(self.tv.indexOf(self.tab_6), _translate("MainWindow", "Вратари"))
        self.tv.setTabText(self.tv.indexOf(self.tab_4), _translate("MainWindow", "Матчи"))
        self.bNextTour.setText(_translate("MainWindow", "Next "))
        self.bExit.setText(_translate("MainWindow", "Exit"))
