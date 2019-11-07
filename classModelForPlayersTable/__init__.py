from PyQt5.Qt import QBrush, QAbstractTableModel, QColor
from PyQt5.QtCore import Qt


class ModelForTablePlayers(QAbstractTableModel):
    def __init__(self, data, func=lambda x: x.name):
        QAbstractTableModel.__init__(self, None)
        self.table_values = data
        self.horizontalHeaderOfTable = ['№', 'Name', 'Club', 'Goals']
        self.func = func
        self.players = sorted(self.table_values, key=self.func, reverse=True)

    def rowCount(self, parent=None, *args, **kwargs):
        return 16

    def columnCount(self, parent=None, *args, **kwargs):
        return len(self.horizontalHeaderOfTable)

    def newData(self):
        self.players = sorted(self.table_values, key=self.func, reverse=True)

    def data(self, index, role=None):
        row = index.row()
        column = index.column()
        if role == Qt.DisplayRole:
            if column == 0:
                return row + 1
            elif column == 1:
                return self.players[row].name
            elif column == 2:
                return self.players[row].club
            elif column == 3:
                return self.players[row].goals
        elif role == Qt.TextAlignmentRole:
            if column != 1:
                return Qt.AlignCenter
        elif role == Qt.BackgroundRole:
            if row == 0:
                return QBrush(QColor(255, 180, 180))
            elif row == 1:
                return QBrush(Qt.darkYellow)
            elif row == 2:
                return QBrush(Qt.green)

    def headerData(self, p_int, Qt_Orientation, role=None):
        if not(role == Qt.DisplayRole):
            return None
        if (Qt_Orientation == Qt.Horizontal):
            return self.horizontalHeaderOfTable[p_int]
        return None


class ModelForTablePlayersPass(QAbstractTableModel):
    def __init__(self, data, func=lambda x: x.name):
        QAbstractTableModel.__init__(self, None)
        self.table_values = data
        self.horizontalHeaderOfTable = ['№', 'Name', 'Club', 'Goals']
        self.func = func
        self.players = sorted(self.table_values, key=self.func, reverse=True)

    def rowCount(self, parent=None, *args, **kwargs):
        return 16

    def columnCount(self, parent=None, *args, **kwargs):
        return len(self.horizontalHeaderOfTable)

    def newData(self):
        self.players = sorted(self.table_values, key=self.func, reverse=True)

    def data(self, index, role=None):
        row = index.row()
        column = index.column()
        if role == Qt.DisplayRole:
            if column == 0:
                return row + 1
            elif column == 1:
                return self.players[row].name
            elif column == 2:
                return self.players[row].club
            elif column == 3:
                if self.players[row].allPass != 0:
                    return str(self.players[row].correctPass / self.players[row].allPass * 100)[:6]
                else:
                    return 0
        elif role == Qt.TextAlignmentRole:
            if column != 1:
                return Qt.AlignCenter
        elif role == Qt.BackgroundRole:
            if row == 0:
                return QBrush(QColor(255, 180, 180))
            elif row == 1:
                return QBrush(Qt.darkYellow)
            elif row == 2:
                return QBrush(Qt.green)

    def headerData(self, p_int, Qt_Orientation, role=None):
        if not(role == Qt.DisplayRole):
            return None
        if (Qt_Orientation == Qt.Horizontal):
            return self.horizontalHeaderOfTable[p_int]
        return None
