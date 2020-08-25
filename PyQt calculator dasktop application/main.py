#!/user/bin/python3
import os
import math
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtQuick import *
from PyQt5.Qt import *


class Button:
    def __init__(self, text, results):
        self.b = QPushButton(str(text))
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda: self.handleInput(self.text))

    def handleInput(self, v):
        if v == "=":
            res = eval(self.results.text())
            self.results.setText(str(res))
        elif v == "AC":
            self.results.setText("")
        elif v == "√":
            value = float(self.results.text())
            self.results.setText(str(math.sqrt(value)))
        elif v == "DEL":
            current_val = self.results.text()
            self.results.setText(current_val[:-1])
        else:
            current_val = self.results.text()
            new_val = current_val + str(v)
            self.results.setText(new_val)


class application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sarthak's calcutaor")
        self.createapp()

    def createapp(self):
        # calculator grid
        grid = QGridLayout()

        result = QLineEdit()
        buttons = ["AC", "DEL", "√", "/",
                   7, 8, 9, "*",
                   4, 5, 6, "-",
                   1, 2, 3, "+",
                   0, ".", "="]

        row = 1
        col = 0

        grid.addWidget(result, 0, 0, 1, 4)
        for button in buttons:
            if col > 3:
                col = 0
                row += 1
            buttonObj = Button(button, result)

            if button == "=":
                grid.addWidget(buttonObj.b, row, col, 1, 2)
            else:
                grid.addWidget(buttonObj.b, row, col, 1, 1)
                col += 1

        self.setLayout(grid)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = application()
    sys.exit(app.exec())
