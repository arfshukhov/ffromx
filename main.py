import pyqtgraph as pg

from dataclasses import dataclass

from functools import partial

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

import sys

from logic import *


@dataclass
class Style:
    background = "background-color: #464c57"
    button_style = """QPushButton
                    {background-color: #216afc; border-radius: 10px; font: bold 14px;min-width: 3em; padding: 1px;
                    color: #212121;} QPushButton:pressed { background-color: #194294; border-radius: 10px;
                    font: bold 14px;min-width: 3em; padding: 1px; color: #212121;}"""
    label = """background-color: green; border-radius: 10px; font: bold 14px;
                                        min-width: 3em; padding: 1px; color: white;"""
    entry_space = """background-color: gray; border-radius: 5px; min-width: 3em; color:
                    white; selection-color: yellow; selection-background-color: blue;"""



class Button(QPushButton):
    def __init__(self, text, function, arg, place):  # arg will be symbol ("1", "+", "/", ...), or fully expression
        super().__init__()

        self.button = QPushButton(text)
        self.button.clicked.connect(partial(function, arg, place))


class ButtonsTable:
    def __init__(self, place):
        self.buttons: list[Button]
        self.buttons = [
            [Button("log(x)", symbol_add, "log()", place).button, Button("sin(α)", symbol_add, "sin()", place).button,
             Button("cos(α)", symbol_add, "cos()", place).button, Button("tg(α)", symbol_add, "tg()", place).button,
             Button(".", symbol_add, ".", place).button],

            [Button("7", symbol_add, "7", place).button, Button("8", symbol_add, "8", place).button,
             Button("9", symbol_add, "9", place).button, Button("+", symbol_add, "+", place).button,
             Button("-", symbol_add, "-", place).button],

            [Button("4", symbol_add, "4", place).button, Button("5", symbol_add, "5", place).button,
             Button("6", symbol_add, "6", place).button, Button("*", symbol_add, "*", place).button,
             Button("/", symbol_add, "/", place).button],

            [Button("1", symbol_add, "1", place).button, Button("2", symbol_add, "2", place).button,
             Button("3", symbol_add, "3", place).button, Button("xʸ", symbol_add, "sqr(x, y)", place).button,
             Button("√", symbol_add, "√()", place).button],

            [NotImplemented, Button("0", symbol_add, "0", place).button,
             Button("X", symbol_add, "x", place).button, Button("(", symbol_add, "(", place).button,
             Button(")", symbol_add, ")", place).button],

        ]


class Graph:
    def __init__(self):
        super().__init__()


        self.plt = pg.plot()
        self.plt.showGrid(x=True,y=True)

        self.plt.setLabel('left', 'Axis', units='y')
        self.plt.setLabel('bottom', 'Axis', units='x')
        self.plt.setLabel('right', 'Axis', units='y')
        self.plt.setLabel('top', 'Axis', units='x')

        range_ = self.plt.getViewBox().viewRange()
        self.plt.setLimits(xMin=-100, xMax=100,
                             yMin=-100, yMax=100)

class Window(QWidget):
    def __init__(self, graphic):
        super().__init__()

        self.setGeometry(100, 100, 1100, 800)
        self.setStyleSheet(Style.background)
        self.setWindowTitle("ffromx - plotting graphs by Larionov software")
        self.icon = QIcon()
        self.icon.addPixmap(QPixmap("hello_html_m2d4d9fc4.png"))
        self.setWindowIcon(self.icon)

        self.range_label = QLabel("range of x", self)
        self.range_label.setGeometry(710, 50, 180, 20)
        self.range_label.setStyleSheet(Style.label)

        self.range_space = QLineEdit(self)
        self.range_space.setGeometry(790, 50, 120, 20)
        self.range_space.setStyleSheet(Style.entry_space)

        self.y_exp = QLabel("y = ", self)
        self.y_exp.setGeometry(710, 25, 15, 20)
        self.y_exp.setStyleSheet(Style.label)

        self.exp_space = QLineEdit(self)
        self.exp_space.setGeometry(737, 25, 300, 20)
        self.exp_space.setStyleSheet(Style.entry_space)

        self.error_label = QTextEdit(self)
        self.error_label.setStyleSheet(Style.label)
        self.error_label.setGeometry(720, 400, 370, 300)

        self.draw_button = QPushButton("draw", self)
        self.draw_button.setGeometry(1040, 20,50,30)
        self.draw_button.clicked.connect(partial(
            execution, self.exp_space, self.range_space, graphic, self.error_label
        ))
        self.draw_button.setStyleSheet(Style.button_style)

        self.lay = QVBoxLayout(self)
        self.lay.addWidget(graphic)

        self.graph_widget = QWidget(self)
        self.graph_widget.setLayout(self.lay)
        self.graph_widget.setGeometry(10,10,700,780)


class Main(QWidget):

    def __init__(self):
        super().__init__()

        self.graph = Graph().plt

        self.window = Window(graphic=self.graph)

        self.grid = QGridLayout()

        self.lay = QWidget(self.window)
        self.lay.setLayout(self.grid)
        self.lay.setGeometry(710, 70, 390, 320)

        self.buttons = ButtonsTable(self.window.exp_space).buttons

        for i, m in enumerate(self.buttons):
            for k, d in enumerate(m):
                if (i + 1, k + 1) == (5, 1):
                    self.btn1 = QPushButton("CE")
                    self.btn1.clicked.connect(partial(break_expression, self.window.exp_space))
                    self.grid.addWidget(self.btn1, i + 1, k + 1)
                    self.btn1.setStyleSheet(Style.button_style)

                else:
                    d.setStyleSheet(Style.button_style)
                    d.resize(50, 50)
                    self.grid.addWidget(d, i + 1, k + 1)

        self.window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    app.exec()