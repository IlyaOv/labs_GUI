import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow, QFileDialog, QMenu, QAction, \
    QVBoxLayout
from PyQt5.QtCore import QRect, Qt, QPoint
from PyQt5.QtGui import QFont, QImage, QPixmap, QPainter, QPen
import cv2 as cv
import os
import numpy as np
import os

class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.white_count = 0
        self.image_name = f"white_{self.white_count}"
        self.image = None
        self.centers = []

        self.setWindowTitle('lab2')

        add_image_action = QAction("Добавить изображение", self)
        add_image_action.triggered.connect(self.add_new_image)

        add_white_image_action = QAction("Добавить белое изображение", self)
        add_white_image_action.triggered.connect(self.add_white_image)

        save_action = QAction("Сохранить центры", self)
        save_action.triggered.connect(self.save)

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('File')
        file_menu.addAction(add_image_action)
        file_menu.addAction(add_white_image_action)
        file_menu.addAction(save_action)

        self.pix = None
        image = self.create_white_image()
        self.add_image(image)
        self.setFixedSize(image.shape[0], image.shape[1])

        self.begin, self.destination = QPoint(), QPoint()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(QPoint(), self.pix)

        if not self.begin.isNull() and not self.destination.isNull():
            rect = QRect(self.begin, self.destination)
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            painter.drawRect(rect.normalized())
            print("not null")
            print(rect.center().x(), rect.center().y())

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.begin = event.pos()
            self.destination = self.begin
            self.update()
            print("mousePressEvent")

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.destination = event.pos()
            self.update()
            print("mouseMoveEvent")

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            rect = QRect(self.begin, self.destination)
            painter = QPainter(self.pix)
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            painter.drawRect(rect.normalized())
            print(rect.center().x(), rect.center().y())
            self.centers.append((rect.center().x(), rect.center().y()))

            self.begin, self.destination = QPoint(), QPoint()
            self.update()
            print("mouseReleaseEvent")

    def read_image(self, path_to_image):
        path_name = os.path.basename(path_to_image)
        self.image_name = path_name.split('.')[0]
        return cv.imread(path_to_image)

    def create_white_image(self):
        image = np.zeros([512, 512, 1], dtype=np.uint8)
        image.fill(255)
        self.white_count += 1
        self.image_name = f"white_{self.white_count}"
        return image

    def add_image(self, image):
        height, width, bytes_per_component = image.shape
        bytes_per_line = 3 * width
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        QImg = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        self.pix = QPixmap.fromImage(QImg)
        self.setFixedSize(self.pix.width(), self.pix.height())
        self.centers = []

    def add_new_image(self):
        path = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a file',
            directory=os.getcwd()
        )[0]
        image = self.read_image(path)
        self.add_image(image)

    def add_white_image(self):
        image = self.create_white_image()
        self.add_image(image)

    def save(self):
        print(self.centers)
        with open(f'centers_{self.image_name}.txt', 'w', encoding='utf-8') as file:
            file.write("Координаты центров прямоугольников:\n")
            for center in self.centers:
                file.write(f"x: {center[0]}, y: {center[1]};\n")


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()