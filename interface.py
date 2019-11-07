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
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.tableViewForTeams = QtWidgets.QTableView(self.tab)
        self.tableViewForTeams.setStyleSheet("QHeaderView {\n"
"    font-size : 16 px;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal {\n"
"    color: #fff;\n"
"    border-style: solid;\n"
"\n"
"    background-color: qlineargradient( x1: 0, y1: 0, x2: 0, y2: 0,\n"
"                                        stop: 0 #4287ff, stop: 1 #356ccc);\n"
" }\n"
"\n"
"QHeaderView::section:first {\n"
"    color: #fff;\n"
" }")
        self.tableViewForTeams.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableViewForTeams.setLineWidth(1)
        self.tableViewForTeams.setSortingEnabled(True)
        self.tableViewForTeams.setObjectName("tableViewForTeams")
        self.tableViewForTeams.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableViewForTeams, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableViewForPlayers = QtWidgets.QTableView(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableViewForPlayers.sizePolicy().hasHeightForWidth())
        self.tableViewForPlayers.setSizePolicy(sizePolicy)
        self.tableViewForPlayers.setAcceptDrops(True)
        self.tableViewForPlayers.setToolTipDuration(-1)
        self.tableViewForPlayers.setStyleSheet("QHeaderView::section {\n"
"     background-color: qlineargradient(x1:0, y1:0, x2:0, y2:0,\n"
"                                       stop:0 #616161, stop: 0.5 #505050,\n"
"                                       stop: 0.6 #434343, stop:1 #656565);\n"
"     color: white;\n"
"     padding-left: 4px;\n"
"     border: 1px solid #6c6c6c;\n"
" }")
        self.tableViewForPlayers.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableViewForPlayers.setObjectName("tableViewForPlayers")
        self.tableViewForPlayers.verticalHeader().setVisible(False)
        self.verticalLayout_4.addWidget(self.tableViewForPlayers)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableViewForPlayersPass = QtWidgets.QTableView(self.tab_3)
        self.tableViewForPlayersPass.setObjectName("tableViewForPlayersPass")
        self.verticalLayout_5.addWidget(self.tableViewForPlayersPass)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.listView = QtWidgets.QListView(self.centralwidget)
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
        self.verticalLayout_2.addWidget(self.listView)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 779, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Футбольный менеджер 2018"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Таблица"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Бомбардирды"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Точные распасовщики"))
        self.pushButton.setText(_translate("MainWindow", "Следующий тур"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
