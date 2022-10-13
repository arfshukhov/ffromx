import pyqtgraph as pg
import pyqtgraph.exporters
import numpy as np

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

import sys


class Graph:
    def __init__(self, range: int, x: list, y: list, ):
        super().__init__()

        self.x = x
        self.y = y

        self.plt = pg.PlotWidget()
        self.plt.showGrid(x=True,y=True)

        self.plt.setLabel('left', 'Axis', units='y')
        self.plt.setLabel('bottom', 'Axis', units='x')
        self.plt.setXRange(-range, range)
        self.plt.setYRange(-range, range)
        self.plt.setWindowTitle('pyqtgraph plot')

        #self.plt.plot(self.x, self. y)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,1100,800)

        self.garph = Graph(50,[1,2,3,4,5],[1,4,9,16,25]).plt

        self.range_label = QLabel("range of x", self)
        self.range_label.setGeometry(710, 500, 180, 50)

        self.range = QLineEdit(self)
        self.range.setGeometry(790, 500, 120, 50)

        self.lay = QVBoxLayout(self)
        self.lay.addWidget(self.garph)

        self.graph_widget = QWidget(self)
        self.graph_widget.setLayout(self.lay)
        self.graph_widget.setGeometry(10,10,700,700)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    app.exec()