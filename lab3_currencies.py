from PyQt5.QtCore import pyqtSignal, QObject


class Dollar(QObject):

    changed_value = pyqtSignal(float)

    def __init__(self, value):
        super().__init__()
        self.value = value

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return round(self.value, 3)

    def updateValue(self, k):
        self.value *= k


class Ruble(QObject):

    changed_value = pyqtSignal(float)

    def __init__(self, value):
        super().__init__()
        self.value = value

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return round(self.value, 3)

    def updateValue(self, k):
        self.value *= k