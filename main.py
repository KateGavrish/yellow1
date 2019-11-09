import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic

import random


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.buttn)
        self.draw1 = False

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        if self.draw1:
            self.update()
            self.draw1 = False
        qp.end()

    def draw(self, qp):
        s = random.randint(4, 50)
        x = random.randint(0, 700)
        y = random.randint(0, 500)
        qp.setBrush(QColor(245, 224, 66))
        qp.drawEllipse(x, y, s, s)

    def buttn(self):
        self.draw1 = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
