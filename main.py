from random import randint
import sys
from PyQt6 import QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.GlobalColor.white)
        self.pushButton.clicked.connect(self.draw_something)
        self.label.setPixmap(canvas)

    def draw_something(self):
        self.setCentralWidget(self.label)
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor('yellow'))
        painter.setPen(pen)
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor("yellow"))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        painter.setBrush(brush)
        w1, w2, w3 = randint(10, 100), randint(10, 100), randint(10, 100)
        painter.drawEllipse(60, 60, w1, w1)
        painter.drawEllipse(200, 220, w2, w2)
        painter.drawEllipse(300, 70, w3, w3)
        painter.end()
        self.label.setPixmap(canvas)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()