class Footballer:
    def __init__(self, id, name, age, workingFoot, height, acceleration, jerkSpeed, positionSelection, completion, impactStrength,
                 longShots, horsebackRiding, penalty, fieldVision, awnings, standards, shortPass,
                 longPass, ballSpin, dexterity, balance, reaction, ballControl, dribbling, selfControl, intercepts,
                 headGame, custody, ballSelection, tackles, jumpingAbility, endurance, force, aggressiveness, club):

        # Неизменяемые характеристики игрока
        self.id = id
        self.name = name
        self.age = age
        self.club = club
        self.workingFoot = workingFoot
        self.height = height

        # Все скрытые характеристики игрока
        self.skillsAll = [acceleration, jerkSpeed, positionSelection, completion, impactStrength,
                 longShots, horsebackRiding, penalty, fieldVision, awnings, standards, shortPass,
                 longPass, ballSpin, dexterity, balance, reaction, ballControl, dribbling, selfControl, intercepts,
                 headGame, custody, ballSelection, tackles, jumpingAbility, endurance, force, aggressiveness, height - 100, 0]

        # Все скиллы игроков(высчитываются по тайной формуле)
        self.skillSave = self.countSkillPosition([0, 1, 3], [5], [2, 4, 29], [30], 21, 0) if self.skillsAll[6] == 0 else 1
        self.skillSelection = self.countSkillPosition([23, 20], [22, 24], [14, 27, 28], [15], 21, 0) if self.skillsAll[6] != 0 else self.skillSave
        self.skillPass = self.countSkillPosition([11, 12], [8, 17], [30], [30], 14, 0) if self.skillsAll[6] != 0 else 1
        self.skillShot = self.countSkillPosition([4, 3], [5, 13], [6, 19], [21], 19, 0) if self.skillsAll[6] != 0 else 1
        self.skills = [self.countSkillPosition([0, 1, 3], [5], [2, 4, 29], [30], 21, 0) if self.skillsAll[6] == 0 else 1,  #skillGoalkeaper
                       self.countSkillPosition([0, 24], [20, 12, 1], [26, 23, 17], [9, 14, 18], 26, -self.workingFoot) if self.skillsAll[6] != 0 else 1,  #skillLeftDefender
                       self.countSkillPosition([23, 27, 22, 21], [20, 24, 25, 29], [28, 1, 19], [0, 11], 37, 0) if self.skillsAll[6] != 0 else 1,  #skillCenterDefender
                       self.countSkillPosition([23, 27, 22, 21], [20, 24, 25, 29], [28, 1, 19], [0, 11], 37, 0) if self.skillsAll[6] != 0 else 1,  #skillCenterDefender
                       self.countSkillPosition([0, 24], [20, 12, 1], [26, 23, 17], [9, 14, 18], 26, +self.workingFoot) if self.skillsAll[6] != 0 else 1,  #skillRightDefender
                       self.countSkillPosition([17, 8, 11], [0, 2, 26], [12, 18, 22, 20], [23, 27, 24, 14], 33, 0) if self.skillsAll[6] != 0 else 1,  #skillCenterMid
                       self.countSkillPosition([17, 8, 11], [0, 2, 26], [12, 18, 22, 20], [23, 27, 24, 14], 33, 0) if self.skillsAll[6] != 0 else 1,  #skillCenterMid
                       self.countSkillPosition([0, 1, 9], [17, 14, 3], [5, 8, 11, 12, 18], [19, 20, 26, 16], 33, -self.workingFoot) if self.skillsAll[6] != 0 else 1,  #skillLeftWinger
                       self.countSkillPosition([17, 8, 11], [12, 0, 14, 5], [3, 18, 26], [20, 2], 32, 0) if self.skillsAll[6] != 0 else 1,  # skillAttackMid
                       self.countSkillPosition([0, 1, 9], [17, 14, 3], [5, 8, 11, 12, 18], [19, 20, 26, 16], 33, +self.workingFoot) if self.skillsAll[6] != 0 else 1,  #skillRightWinger
                       self.countSkillPosition([3, 14], [11, 4], [1, 16, 2, 16, 8, 19, 0, 13], [6, 21, 18, 25, 5, 15], 34, 0) if self.skillsAll[6] != 0 else 1]        #skillStriker

        # Характеристики для каждого сезона
        self.active = False
        self.goals = 0
        self.correctPass = 0
        self.physic = 100
        self.shots = 0
        self.allPass = 0
        self.loseBall = 0
        self.selections = 0
        self.saves = 0

    # Сокращение строк для высчитывания характеристик игроков
    def countSkillPosition(self, for4, for3, for2, for1, count, difference):
        temp = (4 * sum([self.skillsAll[i] for i in for4]) +
               3 * sum([self.skillsAll[i] for i in for3]) +
               2 * sum([self.skillsAll[i] for i in for2]) +
               sum([self.skillsAll[i] for i in for1])) / count
        return temp + difference

    # Восставновление стутуса ACTIVE = False
    def zeroingOfActive(self):
        self.active = False

    def zeroingPhysic(self):
        if self.physic + 300 / self.age >= 100:
            self.physic = 100
        else:
            self.physic += 300 / self.age

