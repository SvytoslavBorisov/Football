import random


class Game:
    def __init__(self, team1, team2):
        # Текущая минута матча
        self.minute = 1
        # Количество мячей, которая забила 1 / 2 команда
        self.homeGoal = 0
        self.guestGoal = 0
        # У какого игрока мяч в данный момент (0 - НomeTeam, 1 - GuestTeam; 1,2,3,4,5,6,7,8,9,10,11 - Позиции на поле)

        #               11(ST)
        #
        #        8(LW)  9(AM)  10(RW)
        #
        #            6(CM) 7(CM)
        #
        #      2(LD) 3(DC) 4(DC) 5(RB)
        #
        #                1(GK)

        self.WhichBall = [0, 0]
        # Вероятность паса одной позиции на другую
        self.positionsOptionsToPass = [[0, 400, 800, 900, 1000, 1050, 1075, 1085, 1095, 1097, 1000, 1000],
                                       [50, 50, 200, 250, 350, 550, 700, 1000, 1005, 1015, 1018, 1025],
                                       [100, 400, 400, 500, 530, 830, 930, 950, 970, 990, 1000, 1050],
                                       [100, 130, 230, 230, 530, 830, 930, 950, 970, 990, 1000, 1050],
                                       [50, 70, 105, 305, 305, 505, 605, 610, 910, 915, 935, 942],
                                       [10, 110, 130, 150, 250, 250, 750, 850, 950, 980, 1010, 1080],
                                       [10, 110, 130, 150, 250, 750, 750, 850, 950, 980, 1010, 1080],
                                       [1, 31, 41, 54, 84, 199, 299, 299, 399, 699, 999, 1099],
                                       [1, 116, 131, 141, 154, 254, 554, 599, 599, 899, 1000, 1100],
                                       [1, 14, 24, 39, 154, 254, 554, 599, 699, 699, 1000, 1100],
                                       [0, 1, 11, 25, 40, 155, 255, 305, 405, 505, 505, 1005]
                                       ]
        # 2 команды, которые играют между собой
        self.teams = [team1, team2]
        self.ids = [team1.id, team2.id]
        self.structures = [[], []]
        self.whoScoreHome = []
        self.whoScoreGuest = []
        self.history = []
        self.mainHistory = []

    # Выбор состава для 2 играющих команд
    def choiceSelection(self):

        # Цикл по 2 командам (1 и 2)
        for j in range(2):

            # Максимальный уровень команды
            maxSkills = 0

            # Индексы игроков для максимального уровня
            dataOfIdMax = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            # Цикл по позициям (11 позиций в футболе)
            for k in range(0, 11):

                # Обнуление активных игроков(все игроки доступны)
                self.teams[j].zeroingOfPlayersActive()

                # Временный максимальный уровень команды
                maxSkillsTEMP = 0

                # Временный список индексов игроков для максимального уровня
                dataOfIdMaxTEMP = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

                # Цикл от k позиции до 11
                for i in range(k, 11):

                    # Получения (индекса игрока, максимального значения позиции) для определенной позиции
                    idTemp, skillTemp = self.teams[j].choicePlayer(i)

                    # Сохраняем значение во временное значение
                    maxSkillsTEMP += skillTemp

                    # Сохраняем индекс во временный список
                    dataOfIdMaxTEMP[i] = idTemp

                    # Устанавливаем для выбранного игрока ACTIVE = True, чтобы его больше нельзя было использовать в оставшихся позициях
                    self.teams[j].players[idTemp].active = True

                # Цикл от 0 до k позиции
                for i in range(0, k):

                    # Получения (индекса игрока, максимального значения позиции) для определенной позиции
                    idTemp, skillTemp = self.teams[j].choicePlayer(i)

                    # Сохраняем значение во временное значение
                    maxSkillsTEMP += skillTemp

                    # Сохраняем индекс во временный список
                    dataOfIdMaxTEMP[i] = idTemp

                    # Устанавливаем для выбранного игрока ACTIVE = True, чтобы его больше нельзя было использовать в оставшихся позициях
                    self.teams[j].players[idTemp].active = True

                # Если временное значение оказалось больше, чем максимальный уровень, то заменяем
                if maxSkills < maxSkillsTEMP:
                    maxSkills = maxSkillsTEMP
                    dataOfIdMax = dataOfIdMaxTEMP

            # Передаем команде индексы игроков, которые будут играть в матче
            self.teams[j].idSostav = list(dataOfIdMax)
            self.structures[j] = list(dataOfIdMax)

    # Проиграть 1 матч между 2 командами
    def match(self):

        # Home team 0/ NumberPosition 6
        self.whichBall = [0, 6]

        # Проход по каждой минуте матча (540 - для большей реалистичности итового результата)
        while self.minute < 540:

            # Для сокращения названия переменных
            wb = self.whichBall[0]
            wb1 = self.whichBall[1]

            # Мяч перемещяется на другую позицию
            self.whichBall = self.passTo(*self.positionsOptionsToPass[wb1 - 1],                 # Опции для данной позиции
                                        self.teams[wb].idSostav[wb1 - 1], wb,                   # id игрока у которого мяч и (0, 1) команды
                                        self.teams[(wb + 1) % 2].idSostav[11 - wb1], 11 - wb1)  # id игрока - сопреника и его позиция
            # Прибавляем минуту
            self.minute += 1

        self.teams[0].zeroingPhysic()
        self.teams[1].zeroingPhysic()
        # Если у 1 команды больше голов, чем у 2, победа присуждается 1
        if self.homeGoal > self.guestGoal:
            self.teams[0].wins += 1
            self.teams[1].defeats += 1

            # За победу присуждается 3 очка
            self.teams[0].points += 3

        # Если у 2 команды больше голов, чем у 1, победа присуждается 2
        elif self.homeGoal < self.guestGoal:
            self.teams[1].wins += 1
            self.teams[0].defeats += 1

            # За победу присуждается 3 очка
            self.teams[1].points += 3

        # Если у 2 команды столько же голов, сколько у 1, ничья
        else:
            self.teams[1].draws += 1
            self.teams[0].draws += 1

            # За ничью присуждается по 1 очку
            self.teams[1].points += 1
            self.teams[0].points += 1

        # Увеличиваем общее количество игр у каждой команды
        self.teams[0].games += 1
        self.teams[1].games += 1

    # Функция паса игрока
    def passTo(self, passToGoalkeaper, passToLeftDefender, passToLeftCenterDefender, passToRightCenterDefender,
               passToRightDefender, passToLeftCenterMid, passToRightCenterNid, passToAttackMid, passToLeftWinger,
               passToRightWinger, passToStriker, PlayerPasNum, # Раскрытие списка positionsOptionsToPass
               idActivePlayerIdTeam, idTeam, idActivePlayerOtherTeam, numberPositionOtherPlayer):

        # Добавление рандома к процессу отбора мяча
        otherPlayersSelection = 1 + random.randint(0, 40)
        randomPass = 1 + random.randint(0, 100)

        # Увеличиваем количество пасов игрока
        self.teams[idTeam].players[idActivePlayerIdTeam].allPass += 1

        # Сокращение переменной
        ps = self.teams[idTeam].players[idActivePlayerIdTeam].physic

        # Изменение физики игрока(совершил действие -> устал, зависимость от возраста)
        self.teams[idTeam].players[idActivePlayerIdTeam].physic -= ps / (self.teams[idTeam].players[idActivePlayerIdTeam].age * 7)

        # Сокращение переменных
        skillSelection = self.teams[(idTeam + 1) % 2].players[idActivePlayerOtherTeam].skillSelection  # Уровень отбора соперника
        skillPass = self.teams[idTeam].players[idActivePlayerIdTeam].skillPass  # Уровень паса игрока

        # Проверяем, удачно ли игрок отдал пас
        if (skillSelection * 2 + otherPlayersSelection <= skillPass * 2 + randomPass) or skillPass == 1: # если это вратарь

            # На какую позицию отдастся пас по роцентному соотношению из positionsOptionsToPass
            playerPass = 1 + random.randint(1, PlayerPasNum)

            # Добавляем игроку 1 удачный пас
            self.teams[idTeam].players[idActivePlayerIdTeam].correctPass += 1

            # Пас голкиперу и т.д.
            if (playerPass > 0) and (playerPass < passToGoalkeaper):
                self.history.append(f'{self.teams[idTeam].players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{self.teams[idTeam].players[self.teams[idTeam].idSostav[0]].name}')
                # Возвращаем команду у которой мяч и номер позиции, везде аналогично
                return [idTeam, 1]
            elif (playerPass > passToGoalkeaper) and (playerPass < passToLeftDefender):
                self.history.append(f'{self.teams[idTeam].players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{self.teams[idTeam].players[self.teams[idTeam].idSostav[1]].name}')
                return [idTeam, 2]
            elif (playerPass > passToLeftDefender) and (playerPass < passToLeftCenterDefender):
                self.history.append(f'{self.teams[idTeam].players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{self.teams[idTeam].players[self.teams[idTeam].idSostav[2]].name}')
                return [idTeam, 3]
            elif (playerPass > passToLeftCenterDefender) and (playerPass < passToRightCenterDefender):
                self.history.append(f'{self.teams[idTeam].players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{self.teams[idTeam].players[self.teams[idTeam].idSostav[3]].name}')
                return [idTeam, 4]
            elif (playerPass > passToRightCenterDefender) and (playerPass < passToRightDefender):
                self.history.append(f'{self.teams[idTeam].players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{self.teams[idTeam].players[self.teams[idTeam].idSostav[4]].name}')
                return [idTeam, 5]
            elif (playerPass > passToRightDefender) and (playerPass < passToLeftCenterMid):
                self.history.append(f'{self.teams[idTeam].players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{self.teams[idTeam].players[self.teams[idTeam].idSostav[5]].name}')
                return [idTeam, 6]
            elif (playerPass > passToLeftCenterMid) and (playerPass < passToRightCenterNid):
                self.history.append(f'{self.teams[idTeam].players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{self.teams[idTeam].players[self.teams[idTeam].idSostav[6]].name}')
                return [idTeam, 7]
            elif (playerPass > passToRightCenterNid) and (playerPass < passToAttackMid):
                self.history.append(f'{self.teams[idTeam].players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{self.teams[idTeam].players[self.teams[idTeam].idSostav[7]].name}')
                return [idTeam, 8]
            elif (playerPass > passToAttackMid) and (playerPass < passToLeftWinger):
                self.history.append(f'{self.teams[idTeam].players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{self.teams[idTeam].players[self.teams[idTeam].idSostav[8]].name}')
                return [idTeam, 9]
            elif (playerPass > passToLeftWinger) and (playerPass < passToRightWinger):
                self.history.append(f'{self.teams[idTeam].players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{self.teams[idTeam].players[self.teams[idTeam].idSostav[9]].name}')
                return [idTeam, 10]
            elif (playerPass > passToRightWinger) and (playerPass < passToStriker):
                self.history.append(f'{self.teams[idTeam].players[idActivePlayerIdTeam].name} отдаёт пас на '
                                    f'{self.teams[idTeam].players[self.teams[idTeam].idSostav[10]].name}')
                return [idTeam, 11]

            # Если не попало в пас, то будет произведён удар
            else:

                # Вычитаем 1 пас, так как игрок будет бить
                self.teams[idTeam].players[idActivePlayerIdTeam].allPass -= 1
                self.teams[idTeam].players[idActivePlayerIdTeam].correctPass -= 1

                # Обращаемся к функции удара, передаем команда, которая бьет, и бьющего игрока
                return self.shot(idTeam, idActivePlayerIdTeam)

        # Если пас неудачен, то игрок другой команды произвел отбор
        else:

            # Прибавляем игроку потерю
            self.teams[idTeam].players[idActivePlayerIdTeam].loseBall += 1
            self.history.append(f'{self.teams[(idTeam + 1) % 2].players[idActivePlayerOtherTeam].name}'
                                f' отобрал мяч у {self.teams[idTeam].players[idActivePlayerIdTeam].name}')

            # Прибавляем игроку отбор
            self.teams[(idTeam + 1) % 2].players[idActivePlayerOtherTeam].selections += 1

            # Возвращаем команду у которой мяч и номер позиции
            return [(idTeam + 1) % 2, numberPositionOtherPlayer + 1]

    # Функция удара
    def shot(self, idTeam, idActivePlayerIdTeam):

        # Добавление рандома к процессу удара
        shotPlayer = random.randint(1, 100 - idTeam * 10)
        saveGoalKeaper = random.randint(1, 711 + idTeam * 10)

        # Сокращение переменных
        skillShot = self.teams[idTeam].players[idActivePlayerIdTeam].skillShot
        skillSave = self.teams[(idTeam + 1) % 2].players[self.teams[(idTeam + 1) % 2].idSostav[0]].skillSave

        # Если удар точен
        if (shotPlayer + skillShot) > (skillSave + saveGoalKeaper):

            # По индексу определяем кому прибавлять гол
            if idTeam:
                self.guestGoal += 1
                self.whoScoreGuest.append([idTeam, idActivePlayerIdTeam])
            else:
                self.homeGoal += 1
                self.whoScoreHome.append([idTeam, idActivePlayerIdTeam])

            # Прибавляем команде 1 забитый гол
            self.teams[idTeam].goals += 1

            # Прибавляем команде 1 пропущенный гол
            self.teams[(idTeam + 1) % 2].loseGoals += 1
            self.history.append(f'{self.teams[idTeam].players[idActivePlayerIdTeam].name} бьёт.... ГОООООООЛ!!!!')
            self.mainHistory.append((f'{self.teams[idTeam].players[idActivePlayerIdTeam].name} ГОЛ', idTeam, self.minute))

            # Прибавляем игроку 1 забитый гол
            self.teams[idTeam].players[idActivePlayerIdTeam].goals += 1

            # Возвращаем индекс пропустившей команды, и разыгрывающего игрока
            return [(idTeam + 1) % 2, 6]

        # Если удар не точен
        else:

            # Добавляем рандома к процессу сейва
            t = 1 + random.randint(1, 10)

            # Если вратарь отбил то прибаляем вратарю сейв, иначе игрок ударил мимо
            if t >= 9:
                self.teams[(idTeam + 1) % 2].players[self.teams[(idTeam + 1) % 2].idSostav[0]].saves += 1
                self.history.append(f'{self.teams[idTeam].players[idActivePlayerIdTeam].name} бьёт... '
                                    f'{self.teams[(idTeam + 1) % 2].players[self.teams[(idTeam + 1) % 2].idSostav[0]].name} отбивает!')
            else:
                self.history.append(f'{self.teams[idTeam].players[idActivePlayerIdTeam].name} бьёт... МИМО!!')

            # Возвращаем команду у которой мяч и номер позиции
            return [(idTeam + 1) % 2, 1]

    def returnResult(self):
        return f'{self.homeGoal}:{self.guestGoal}'

    def returnSostav(self):
        stTemp = ''
        dataPlayer1Team = []
        dataPlayer2Team = []
        for i in range(11):
            dataPlayer1Team.append(self.teams[0].returnPlayerOnPosition(i))
            dataPlayer2Team.append(self.teams[1].returnPlayerOnPosition(i))
        maxLenPlayer = max(dataPlayer1Team, key=lambda x: len(x))
        for i in range(11):
            stTemp += dataPlayer1Team[i] + ' ' * (10 + len(maxLenPlayer) - len(dataPlayer1Team[i])) + dataPlayer2Team[i] + '\n'
        return stTemp