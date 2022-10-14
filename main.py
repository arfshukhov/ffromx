import pyqtgraph as pg

from dataclasses import dataclass

from functools import partial

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

import sys

from logic import *


class Graph:
    def __init__(self, range: int, x: list, y: list, ):
        super().__init__()

        self.x = x
        self.y = y

        self.plt = pg.plot()
        self.plt.showGrid(x=True,y=True)

        self.plt.setLabel('left', 'Axis', units='y')
        self.plt.setLabel('bottom', 'Axis', units='x')
        #self.plt.setXRange(-range, range)
        #self.plt.setYRange(-range, range)
        range_ = self.plt.getViewBox().viewRange()
        #self.plt.setLimits(xMin=-range, xMax=range,
        #                     yMin=-range, yMax=range)
        #self.plt.setLimits(-range, range)
        self.plt.setWindowTitle('pyqtgraph plot')

        #self.plt.plot(self.x, self. y)


class Window(QWidget):
    def __init__(self, graphic):
        super().__init__()
        #self.graph = Graph(50, [1, 2, 3, 4, 5], [1, 4, 9, 16, 25]).plt
        self.setGeometry(100, 100, 1100, 800)

        self.range_label = QLabel("range of x", self)
        self.range_label.setGeometry(710, 500, 180, 50)

        self.range_space = QLineEdit(self)
        self.range_space.setGeometry(790, 500, 120, 50)

        self.y_exp = QLabel("range of x", self)
        self.y_exp.setGeometry(710, 10, 180, 50)

        self.exp_space = QLineEdit(self)
        self.exp_space.setGeometry(790, 10, 120, 50)

        self.draw_button = QPushButton("draw", self)
        self.draw_button.setGeometry(1000,10,50,30)
        self.draw_button.clicked.connect(partial(execution, self.exp_space, self.range_space, graphic))

        self.lay = QVBoxLayout(self)
        self.lay.addWidget(graphic)

        self.graph_widget = QWidget(self)
        self.graph_widget.setLayout(self.lay)
        self.graph_widget.setGeometry(10,10,700,700)

        self.show()

class Main:
    def __init__(self):
        super().__init__()
        self.graph = Graph(50, [1, 2, 3, 4, 5], [1, 4, 9, 16, 25]).plt
        self.window = Window(graphic=self.graph)






    def get_text(self):
        return int(self.range_space.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    app.exec()