import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.do_paint = True
        self.paint()

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        width = MyWidget().frameGeometry().width()
        height = MyWidget().frameGeometry().height()
        a = random.choice(range(0, width))
        b = random.choice(range(0, height))
        if a >= b:
            c = random.choice(range(0, width - a))
        else:
            c = random.choice(range(0, height - b))
        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(a, b, c, c)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
