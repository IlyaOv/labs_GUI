from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5.uic import loadUi
from lab3_currencies import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = loadUi("generator.ui", self)
        self.oil_value = 79.41
        self.dollar = Dollar(73.09)
        self.ruble = Ruble(0.014)
        self.dollar.changed_value.connect(self.dollar.updateValue)
        self.ruble.changed_value.connect(self.ruble.updateValue)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Генератор курсов валют")
        self.setFixedSize(326, 191)

        self.doubleSpinBox.setValue(self.oil_value)

        self.lineEdit.setText(str(self.dollar.getValue()))
        self.lineEdit.setEnabled(False)

        self.lineEdit_2.setText(str(self.ruble.getValue()))
        self.lineEdit_2.setEnabled(False)

        self.pushButton.clicked.connect(self.analysis)

    def analysis(self):
        new_value = self.doubleSpinBox.value()
        old_value = self.oil_value
        if new_value != old_value:
            k = new_value/old_value
            k_d, k_r = 1/k, k
            self.dollar.changed_value.emit(k_d)
            self.ruble.changed_value.emit(k_r)
            self.oil_value = new_value
            self.lineEdit.setText(str(self.dollar.getValue()))
            self.lineEdit_2.setText(str(self.ruble.getValue()))


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
