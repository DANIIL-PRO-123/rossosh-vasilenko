from random import randint
from PyQt6.QtCore import Qt
from PyQt6 import QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QApplication
import sys


class Form(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        canvas = QtGui.QPixmap(391, 241)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        random_size = randint(10, 200)
        canvas = QtGui.QPixmap(391, 241)
        canvas.fill(Qt.GlobalColor.white)
        painter = QtGui.QPainter(canvas)

        pen = QtGui.QPen()
        pen.setWidth(5)
        pen.setColor(QtGui.QColor(240, 216, 65))
        painter.setPen(pen)
        painter.drawEllipse(391 // 2 - random_size // 2, 241 // 2 - random_size // 2, random_size, random_size)
        painter.end()
        self.label.setPixmap(canvas)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec())
