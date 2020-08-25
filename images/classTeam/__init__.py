import sqlite3
from classFootballer import Footballer


class Team:
    def __init__(self, id, name, liga):
        # id команды
        self.id = id
        # Название команды
        self.name = name
        # Количество побед команды
        self.wins = 0
        # Количество поражений
        self.defeats = 0
        # Количество ничьих
        self.draws = 0
        # Количество игр
        self.games = 0
        # Чеспионат(?)
        self.liga = liga
        # Количество забитых мячей
        self.goals = 0
        # Количество очков
        self.points = 0
        # Количество пропущенных мячей
        self.loseGoals = 0
        # Список игроков
        self.players = self.getPlayers()
        # Текущий состав команды(выбирается перед матчем)
        self.idSostav = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        self.arrayOfGames = []

    # Обращение к БД для взятие игроков
    def getPlayers(self):

        con = sqlite3.connect('FootballManager.db')
        cur = con.cursor()
        # Обращение к БД для взятие игроков именно этой команды
        result = cur.execute('SELECT * FROM players where club IN (select id from teams where title = "{}")'.format(self.name)).fetchall()
        con.close()

        # Временная список игроков
        dataOfPlayersTEMP = []

        # Идем по всем подходящим игрокам
        for x in result:

            # Исключаем команду, добавляя ее потом
            dataTemp = x[:2] + x[3:]
            dataOfPlayersTEMP.append(Footballer(*dataTemp, self.name))  # <- в конец добавляем название команды

        # Возвращаем список игроков этой команды
        return dataOfPlayersTEMP

    # Функция выюора игрока на данную позицию(idPosition)
    def choicePlayer(self, idPosition):

        # Переменные для поиска лучшего игрока для данной позиции
        maxAttribute = 0
        maxPhysic = 0
        idPlayer = 0

        # Идем по всем игрокам команды
        for i, footballer in enumerate(self.players):

            # Если игрок ещё не выбран был, а и его характеристики подходят
            if (maxAttribute * maxPhysic <= footballer.skills[idPosition] * footballer.physic) and footballer.active == False:
                maxAttribute = footballer.skills[idPosition]
                maxPhysic = footballer.physic
                idPlayer = i

        # Возвращаем id игрока и его характеристику для данной позиции
        return idPlayer, maxAttribute

    # Восстановление всем игрокам команды статуса ACTIVE = False
    def zeroingOfPlayersActive(self):
        for i in range(len(self.players)):
            self.players[i].zeroingOfActive()

    # Обнуление всех характеристик команды и их игроков перед новым сезоном
    def zeroingOfNewSeason(self):
        self.points = 0
        self.games = 0
        self.wins = 0
        self.defeats = 0
        self.draws = 0
        self.goals = 0
        self.loseGoals = 0
        for i in range(len(self.players)):
            self.players[i].goals = 0
            self.players[i].allPass = 0
            self.players[i].correctPass = 0
            self.players[i].loseBall = 0
            self.players[i].shots = 0
            self.players[i].saves = 0
            self.players[i].physic = 100

    def returnPlayerOnPosition(self, idPosition):
        stTemp = self.players[self.idSostav[idPosition]].name
        return stTemp

    def zeroingPhysic(self):
        for i in range(len(self.players)):
            self.players[i].zeroingPhysic()