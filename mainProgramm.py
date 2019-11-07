import sqlite3
import sys
from classTeam import Team
from classLiga import Liga
from classModelForTeamsTable import ModelForTableTeams
from classModelForPlayersTable import ModelForTablePlayers, ModelForTablePlayersPass
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QAbstractItemView, QStyleFactory, qApp
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from interface import Ui_MainWindow

class Interface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        qApp.setStyle(QStyleFactory.create("Fusion"))
        # Считывание данных из БД, таблицы 'teams'
        con = sqlite3.connect('FootballManager.db')
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM teams""").fetchall()
        con.close()

        # Заполнение класса Team, извлеченными данными
        self.arrayOfTeams = []
        for x in result:
            self.arrayOfTeams.append(Team(x[0], x[1], x[2]))

        # Создание списка сезонов(состоит из игр -> команд -> игроков), каждый прошедший сезон сохраняется в отдельном файле, как архив
        self.globalNumberSeason = 0
        self.ligas = [Liga(self.arrayOfTeams[:16], self.globalNumberSeason)]


        self.model = QStandardItemModel()
        self.listView.setModel(self.model)
        self.listView.clicked.connect(self.onListView)
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)


        # Создание модели для таблицы команд
        self.modelForTableTeams = ModelForTableTeams(self.ligas[-1])

        self.filterModelForTableTeams = QSortFilterProxyModel()
        self.filterModelForTableTeams.setSourceModel(self.modelForTableTeams)
        self.tableViewForTeams.setModel(self.filterModelForTableTeams)

        self.tableViewForTeams.setSortingEnabled(False)
        #self.tableViewForTeams.sortByColumn(0, Qt.AscendingOrder)

        self.tableViewForTeams.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableViewForTeams.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableViewForTeams.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableViewForTeams.setFont(QFont("times", 12))
        self.tableViewForTeams.clicked.connect(self.openGame)

        # Создание модели для таблицы лучших бомбардиров
        self.modelForTablePlayers = ModelForTablePlayers(self.ligas[-1].allPlayers, func=lambda x: (x.goals, x.name))

        self.filterModelForTablePlayers = QSortFilterProxyModel()
        self.filterModelForTablePlayers.setSourceModel(self.modelForTablePlayers)
        self.tableViewForPlayers.setModel(self.filterModelForTablePlayers)

        self.tableViewForPlayers.setSortingEnabled(False)
        #self.tableViewForPlayers.sortByColumn(0, Qt.AscendingOrder)

        self.tableViewForPlayers.setFont(QFont("times", 16))
        self.tableViewForPlayers.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableViewForPlayers.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableViewForPlayers.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Создание модели для таблицы лучших распасовщиков
        self.modelForTablePlayersPass = ModelForTablePlayersPass(self.ligas[-1].allPlayers,
                                                            func=lambda x: (x.correctPass / (x.allPass * 100), x.name) if x.skillPass != 1 and x.allPass != 0 else (0, x.name))

        self.filterModelForTablePlayersPass = QSortFilterProxyModel()
        self.filterModelForTablePlayersPass.setSourceModel(self.modelForTablePlayersPass)
        self.tableViewForPlayersPass.setModel(self.filterModelForTablePlayersPass)

        self.tableViewForPlayersPass.setSortingEnabled(False)
        #self.tableViewForPlayers.sortByColumn(0, Qt.AscendingOrder)

        self.tableViewForPlayersPass.setFont(QFont("times", 16))
        self.tableViewForPlayersPass.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableViewForPlayersPass.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableViewForPlayersPass.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Обновление таблиц
        self.onlineTables()

        self.pushButton.clicked.connect(self.playOneTour)

    # Проигровка 1 тура матчей лиги
    def playOneTour(self):

        # Если текущий тур не ушёл за границы дозволенного, то продолжить увеличивать туры
        if self.ligas[self.globalNumberSeason].tourNow != (self.ligas[self.globalNumberSeason].countTeams - 1) * 2:

            # Сыграть тур
            self.ligas[self.globalNumberSeason].playTour()

            item = QStandardItem(f'Tур {self.ligas[self.globalNumberSeason].tourNow + 1}\n')
            self.model.appendRow(item)

            #for i in range(self.ligas[self.globalNumberSeason].tourNow *
            #               self.ligas[self.globalNumberSeason].countTeams // 2,
            #               (self.ligas[self.globalNumberSeason].tourNow + 1) *
            #               self.ligas[self.globalNumberSeason].countTeams // 2):
            #    self.textEdit.insertPlainText(self.ligas[self.globalNumberSeason].games[i].teams[0].name + ' ' +
            #                                  str(self.ligas[self.globalNumberSeason].games[i].homeGoal) + ':' +
            #                                  str(self.ligas[self.globalNumberSeason].games[i].guestGoal) + ' ' +
            #                                  self.ligas[self.globalNumberSeason].games[i].teams[1].name + '\n')
            #self.textEdit.insertPlainText('\n')
            # self.textEdit.insertPlainText('-------------------------------------\n')

            # Обновление таблиц
            self.ligas[self.globalNumberSeason].tourNow += 1
            self.onlineTables()
        else:

            with open(f'season{self.globalNumberSeason}.txt', 'w') as f:
                for i in range(self.modelForTableTeams.rowCount()):
                    f.write(self.modelForTableTeams.teams[i].name + ' ' + str(self.modelForTableTeams.teams[i].points) + '\n')

            # Обнуляем все значения для нового сезона
            for i in range(len(self.ligas[self.globalNumberSeason].teams)):
                self.ligas[self.globalNumberSeason].teams[i].zeroingOfNewSeason()

            # Увеличиваем номер сезона на 1
            self.globalNumberSeason += 1

            # Создание нового сезона
            self.ligas.append(Liga(self.arrayOfTeams[:16], self.globalNumberSeason))
            self.modelForTableTeams.newDatas(self.ligas[-1])

            # Обновление таблиц
            self.onlineTables()
            self.model.clear()

    def onlineTables(self):

        # Обновление данных таблиц
        self.modelForTableTeams.oneSort()
        startIndex = self.modelForTableTeams.createIndex(0, 0)
        stopIndex = self.modelForTableTeams.createIndex(self.modelForTableTeams.rowCount(),
                                                        self.modelForTableTeams.columnCount())
        self.tableViewForTeams.dataChanged(startIndex, stopIndex)

        # Обновление данных таблиц
        self.modelForTablePlayers.newData()
        startIndex = self.modelForTablePlayers.createIndex(0, 0)
        stopIndex = self.modelForTablePlayers.createIndex(self.modelForTablePlayers.rowCount(),
                                                          self.modelForTablePlayers.columnCount())

        self.tableViewForPlayers.dataChanged(startIndex, stopIndex)

        # Обновление данных таблиц
        self.modelForTablePlayersPass.newData()
        startIndex = self.modelForTablePlayersPass.createIndex(0, 0)
        stopIndex = self.modelForTablePlayersPass.createIndex(self.modelForTablePlayersPass.rowCount(),
                                                          self.modelForTablePlayersPass.columnCount())

        self.tableViewForPlayersPass.dataChanged(startIndex, stopIndex)

        # Изменение таблицы команд под новые данные
        self.tableViewForTeams.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableViewForTeams.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableViewForTeams.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Изменение таблицы бомбардиров под новые данные
        self.tableViewForPlayers.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableViewForPlayers.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableViewForPlayers.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Изменение таблицы бомбардиров под новые данные
        self.tableViewForPlayersPass.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableViewForPlayersPass.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableViewForPlayersPass.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def openGame(self, index):
        row = index.row()
        column = index.column()
        if 2 <= column < 18:
            if column - 2 != row:
                temp = self.modelForTableTeams.table_values.findGameForIds(
                    [self.modelForTableTeams.teams[row].id,
                     self.modelForTableTeams.teams[column - 2].id])
                if temp:
                    print(temp.teams[0].name + ' ' + str(temp.homeGoal) + ' ' + ':' + ' ' + str(temp.guestGoal) + ' ' + temp.teams[1].name)
                    for i in range(2):
                        for x in temp.structures[i]:
                            print(temp.teams[i].players[x].name, temp.teams[i].players[x].physic)
                        print()

    def onListView(self, index):
        row = index.row()
        stTemp2 = str(self.model.item(row).text())
        stTempClick0 = str(stTemp2).split()[0]
        stTempClick1 = stTemp2.split()[1]
        if stTempClick0 == 'Tур':
            if row + 1 == self.model.rowCount():
                for i in range(self.ligas[-1].countTeams // 2):
                    team1 = self.ligas[-1].findGameForIds(self.ligas[-1].games[int(stTempClick1) - 1][i].ids).teams[0].name
                    result = self.ligas[-1].findGameForIds(self.ligas[-1].games[int(stTempClick1) - 1][i].ids).returnResult()
                    team2 = self.ligas[-1].findGameForIds(self.ligas[-1].games[int(stTempClick1) - 1][i].ids).teams[1].name
                    stTemp = f'{team1} {result} {team2}'
                    item = QStandardItem(stTemp)
                    self.model.insertRow(row + 1, item)
            else:
                stTemp3 = str(self.model.item(row + 1).text())
                stTempClick2 = str(stTemp3).split()[0]
                if stTempClick2 == 'Tур':
                    for i in range(self.ligas[-1].countTeams // 2):
                        team1 = self.ligas[-1].findGameForIds(self.ligas[-1].games[int(stTempClick1) - 1][i].ids).teams[0].name
                        result = self.ligas[-1].findGameForIds(self.ligas[-1].games[int(stTempClick1) - 1][i].ids).returnResult()
                        team2 = self.ligas[-1].findGameForIds(self.ligas[-1].games[int(stTempClick1) - 1][i].ids).teams[1].name
                        stTemp = f'{team1} {result} {team2}'
                        item = QStandardItem(stTemp)
                        self.model.insertRow(row + 1, item)
                else:
                    j = 0
                    stTempClick4 = ''
                    print(6)
                    while stTempClick4 != 'Tур' and j + row + 1 < self.model.rowCount():
                        print(stTempClick4, j + row)
                        j += 1
                        stTemp4 = str(self.model.item(j + row).text())
                        stTempClick4 = str(stTemp4).split()[0]
                    if stTempClick4 != 'Tур':
                        for i in range(j):
                            self.model.removeRow(row + 1)
                    else:
                        for i in range(j - 1):
                            self.model.removeRow(row + 1)
        else:
            if ':' in stTemp2:
                if row + 1 != self.model.rowCount():
                    temp1 = str(self.model.item(row + 1).text())
                    if ':' in temp1 or 'Tур' in temp1:
                        temp = stTemp2.split(':')
                        name1 = ' '.join(temp[0].split()[:-1])
                        name2 = ' '.join(temp[1].split()[1:])
                        game = self.ligas[-1].findGameForNames(name1, name2)
                        if game:
                            item = QStandardItem(game.returnSostav())
                            self.model.insertRow(row + 1, item)
                    else:
                        self.model.removeRow(row + 1)
                else:
                    temp = stTemp2.split(':')
                    name1 = ' '.join(temp[0].split()[:-1])
                    name2 = ' '.join(temp[1].split()[1:])
                    game = self.ligas[-1].findGameForNames(name1, name2)
                    if game:
                        item = QStandardItem(game.returnSostav())
                        self.model.insertRow(row + 1, item)

app = QApplication(sys.argv)
ex = Interface()
ex.show()
sys.exit(app.exec_())