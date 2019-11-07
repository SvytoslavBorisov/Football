from PyQt5.Qt import QBrush, QAbstractTableModel, QColor
from PyQt5.QtCore import Qt


class ModelForTableTeams(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self, None)
        self.table_values = data
        self.teams = sorted(self.table_values.teams, key=lambda x: (x.points, x.goals - x.loseGoals, x.goals, x.wins),
                            reverse=True)
        numbers = [str(i + 1) for i in range(16)]
        self.horizontalHeaderOfTable = ['№', 'Team'] + numbers + ['*', 'M.', 'W.', 'D.', 'L.', 'Goals', 'Points']

    def rowCount(self, parent=None, *args, **kwargs):
        return self.table_values.countTeams

    def columnCount(self, parent=None, *args, **kwargs):
        return 25

    def oneSort(self):
        self.teams = sorted(self.table_values.teams, key=lambda x: (x.points, x.goals - x.loseGoals, x.goals, x.wins), reverse=True)

    def newDatas(self, newData):
        self.table_values = newData

    def data(self, index, role=None):
        row = index.row()
        column = index.column()
        if role == Qt.DisplayRole:
            if column == 0:
                return row + 1
            elif column == 1:
                return self.teams[row].name
            elif column < 18:
                if column - 2 != row:
                    temp = self.table_values.findGameForIds([self.teams[row].id, self.teams[column - 2].id])
                    if temp:
                        return temp.returnResult()
                    else:
                        return ''
                return '***'
            elif column == 19:
                return self.teams[row].games
            elif column == 20:
                return self.teams[row].wins
            elif column == 21:
                return self.teams[row].draws
            elif column == 22:
                return self.teams[row].defeats
            elif column == 23:
                return str(self.teams[row].goals) + ':' + str(self.teams[row].loseGoals)
            elif column == 24:
                return self.teams[row].points
        elif role == Qt.TextAlignmentRole:
            if column != 1:
                return Qt.AlignCenter
        elif role == Qt.BackgroundRole:
            if column < 1:
                return QBrush(QColor(180, 180, 255))
            if column == 1:
                if row == 0:
                    return
            if 2 <= column < 18:
                if column - 2 != row:
                    temp = self.table_values.findGameForIds([self.teams[row].id, self.teams[column - 2].id])
                    if temp:
                        if temp.homeGoal > temp.guestGoal:
                            return QBrush(QColor(180, 250, 180))
                        elif temp.homeGoal == temp.guestGoal:
                            return QBrush(QColor(255, 255, 66))
                        else:
                            return QBrush(QColor(255, 100, 100))
                else:
                    return QBrush(Qt.black)
        return

    def headerData(self, p_int, Qt_Orientation, role=None):
        if not(role == Qt.DisplayRole):
            return None
        if (Qt_Orientation == Qt.Horizontal):
            return self.horizontalHeaderOfTable[p_int]
        return None

    def sort(self, p_int, order=None):
        if p_int == 1:
            self.teams = sorted(self.table_values, key=lambda x: x.name)