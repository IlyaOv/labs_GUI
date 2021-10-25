import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QFont


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('lab1')
        self.setGeometry(800, 600, 200, 200)

        self.btn = QPushButton(self)
        self.btn.move(10, 10)
        self.btn.setText("Нажмите на кнопку")
        self.btn.adjustSize()
        self.btn.clicked.connect(self.add_text)

        self.msg = QLabel(self)
        self.msg.move(10, 50)
        self.msg.setFont(QFont('Arial', 12))

    def add_text(self):
        self.msg.setText("Кнопка сработала")
        self.msg.adjustSize()


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()