from random import randint
from PyQt6.QtCore import Qt
from PyQt6 import QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QApplication
import sys
from PyQt6 import QtCore


class Form(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        canvas = QtGui.QPixmap(391, 241)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.pushButton.clicked.connect(self.run)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(704, 500)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 370, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 50, 391, 241))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Показать окружность"))


    def run(self):
        random_size = randint(10, 200)
        canvas = QtGui.QPixmap(391, 241)
        canvas.fill(Qt.GlobalColor.white)
        painter = QtGui.QPainter(canvas)

        pen = QtGui.QPen()
        pen.setWidth(5)
        pen.setColor(QtGui.QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        painter.setPen(pen)
        painter.drawEllipse(391 // 2 - random_size // 2, 241 // 2 - random_size // 2, random_size, random_size)
        painter.end()
        self.label.setPixmap(canvas)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec())
