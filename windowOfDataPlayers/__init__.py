import sqlite3
import sys
from classTeam import Team
from classLiga import Liga
from classModelForTeamsTable import ModelForTableTeams
from classModelForPlayersTable import ModelForTablePlayers, ModelForTablePlayersPass
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QAbstractItemView, QStyleFactory,\
    qApp, QWidget, QDataWidgetMapper
from PyQt5.QtCore import Qt, QSortFilterProxyModel,QItemSelectionModel
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5 import QtSql
from playersData import Ui_MainWindow

class BaseDataPlayers(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("FootballManager.db")
        db.open()
        self.model = QtSql.QSqlRelationalTableModel(self.tableView)
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.setTable("players")

        nameIdx = self.model.fieldIndex("name")
        clubIdx = self.model.fieldIndex("club")
        ageIdx = self.model.fieldIndex("age")
        workingFootIdx = self.model.fieldIndex("workingFoot")
        heightIdx = self.model.fieldIndex("height")
        accelerationIdx = self.model.fieldIndex("acceleration")
        jerkSpeedIdx = self.model.fieldIndex("jerkSpeed")
        positionSelectionIdx = self.model.fieldIndex("positionSelection")
        completionIdx = self.model.fieldIndex("completion")
        impactStrengthIdx = self.model.fieldIndex("impactStrength")
        longShotsIdx = self.model.fieldIndex("longShots")
        horsebackRidingIdx = self.model.fieldIndex("horsebackRiding")
        penaltyIdx = self.model.fieldIndex("penalty")
        fieldVisionIdx = self.model.fieldIndex("fieldVision")
        awningsIdx = self.model.fieldIndex("awnings")
        standardsIdx = self.model.fieldIndex("standards")
        shortPassIdx = self.model.fieldIndex("shortPass")
        longPassIdx = self.model.fieldIndex("longPass")
        ballSpinIdx = self.model.fieldIndex("ballSpin")
        dexterityIdx = self.model.fieldIndex("dexterity")
        balanceIdx = self.model.fieldIndex("balance")
        reactionIdx = self.model.fieldIndex("reaction")
        ballControlIdx = self.model.fieldIndex("ballControl")
        dribblingIdx = self.model.fieldIndex("dribbling")
        selfControlIdx = self.model.fieldIndex("selfControl")
        interceptsIdx = self.model.fieldIndex("intercepts")
        headGameIdx = self.model.fieldIndex("headGame")
        custodyIdx = self.model.fieldIndex("custody")
        ballSelectionIdx = self.model.fieldIndex("ballSelection")
        tacklesIdx = self.model.fieldIndex("tackles")
        jumpingAbilityIdx = self.model.fieldIndex("jumpingAbility")
        enduranceIdx = self.model.fieldIndex("endurance")
        forceIdx = self.model.fieldIndex("force")
        aggressivenessIdx = self.model.fieldIndex("aggressiveness")

        # устанавливаем связь по полю club
        self.model.setRelation(clubIdx, QtSql.QSqlRelation("teams", "id", "title"))

        # Запускае модель
        self.model.select()
        self.tableView.setModel(self.model)

        self.tableView.setColumnHidden(self.model.fieldIndex("id"), True)

        # Настройки таблицы
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.model.setHeaderData(1, Qt.Horizontal, "Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Club")
        self.model.setHeaderData(3, Qt.Horizontal, "Age")

        #self.tableView.setColumnWidth(3, 80)
        #self.tableView.setColumnWidth(4, 100)

        # Создаем Mapper для отображения БД на lineEdit - ы
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setModel(self.model)

        # создаем mapping для полей БД на lineEdit - ы по индексам
        self.mapper.addMapping(self.lineName, nameIdx);
        self.mapper.addMapping(self.lineTeam, clubIdx);
        self.mapper.addMapping(self.lineAge, ageIdx);
        self.mapper.addMapping(self.lineWorkingFoot, workingFootIdx);
        self.mapper.addMapping(self.lineHeight, heightIdx);
        self.mapper.addMapping(self.lineAcceleration, accelerationIdx);
        self.mapper.addMapping(self.lineJerkSpeed, jerkSpeedIdx);
        self.mapper.addMapping(self.linePositionSelection, positionSelectionIdx);
        self.mapper.addMapping(self.lineCompletion, completionIdx);
        self.mapper.addMapping(self.lineImpactStrength, impactStrengthIdx);
        self.mapper.addMapping(self.lineLongShots, longShotsIdx);
        self.mapper.addMapping(self.lineHorsebackRiding, horsebackRidingIdx);
        self.mapper.addMapping(self.linePenalty, penaltyIdx);
        self.mapper.addMapping(self.lineFieldVision, fieldVisionIdx);
        self.mapper.addMapping(self.lineAwnings, awningsIdx);
        self.mapper.addMapping(self.lineStandards, standardsIdx);
        self.mapper.addMapping(self.lineShortPass, shortPassIdx);
        self.mapper.addMapping(self.lineLongPass, longPassIdx);
        self.mapper.addMapping(self.lineBallSpin, ballSpinIdx);
        self.mapper.addMapping(self.lineDexterity, dexterityIdx);
        self.mapper.addMapping(self.lineBalance, balanceIdx);
        self.mapper.addMapping(self.lineReaction, reactionIdx);
        self.mapper.addMapping(self.lineBallControl, ballControlIdx);
        self.mapper.addMapping(self.lineDribbling, dribblingIdx);
        self.mapper.addMapping(self.lineSelfControl, selfControlIdx);
        self.mapper.addMapping(self.lineIntercepts, interceptsIdx);
        self.mapper.addMapping(self.lineHeadGame, headGameIdx);
        self.mapper.addMapping(self.lineCustody, custodyIdx);
        self.mapper.addMapping(self.lineBallSelection, ballSelectionIdx);
        self.mapper.addMapping(self.lineTackles, tacklesIdx);
        self.mapper.addMapping(self.lineJumpingAbility, jumpingAbilityIdx);
        self.mapper.addMapping(self.lineEndurance, enduranceIdx);
        self.mapper.addMapping(self.lineForce, forceIdx);
        self.mapper.addMapping(self.lineAggressiveness, aggressivenessIdx);

        # связываем изменения в модели с mapper
        self.tableView.selectionModel().currentRowChanged.connect(self.mapper.setCurrentModelIndex)

        # текущий индекс таблицы
        self.tableView.setCurrentIndex(self.model.index(0, 0))
        self.pExit.clicked.connect(self.closeWindow)
        self.pNext.clicked.connect(self.mapper.toNext)
        self.pLast.clicked.connect(self.mapper.toLast)
        self.pSave.clicked.connect(self.save)
        self.pPrevious.clicked.connect(self.mapper.toPrevious)
        self.pStart.clicked.connect(self.mapper.toFirst)
        self.tableView.scrollTo(self.tableView.currentIndex())

    def save(self):
        #сохраняем данные
        self.model.submitAll()

    def closeWindow(self):
        self.close()