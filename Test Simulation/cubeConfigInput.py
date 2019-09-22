from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import random
from CubeRenderer import CubeRenderer
from PyQt5.QtWidgets import (QAction, QApplication, QGridLayout, QMainWindow, QScrollArea, QSizePolicy, QSlider, QWidget)
from CubeRenderer import CubeRenderer
from PyQt5.QtCore import Qt
import sys
import keyboard
# from cube_driver import *


class PyQtWindow(QMainWindow):
    def __init__(self):
        # app = QApplication([])
        super().__init__()

        self.title = 'Cube Solver'


        uic.loadUi("CubeConfigLayout.ui", self)

        # dropdown options for color combo
        self.title = 'Cube Solver'


        self.colorBox.addItem("Red")
        self.colorBox.addItem("Orange")
        self.colorBox.addItem("Blue")
        self.colorBox.addItem("Green")
        self.colorBox.addItem("White")
        self.colorBox.addItem("Yellow")

        # dropdown options for edit color combo
        self.EditColorBox.addItem("Add Color")
        self.EditColorBox.addItem("Clear Color")

        # L side button click events
        self.L00.clicked.connect(lambda: self.buttonPressed(self.L00))
        self.L01.clicked.connect(lambda: self.buttonPressed(self.L01))
        self.L02.clicked.connect(lambda: self.buttonPressed(self.L02))
        self.L10.clicked.connect(lambda: self.buttonPressed(self.L10))
        self.L11.clicked.connect(lambda: self.buttonPressed(self.L11))
        self.L12.clicked.connect(lambda: self.buttonPressed(self.L12))
        self.L20.clicked.connect(lambda: self.buttonPressed(self.L20))
        self.L21.clicked.connect(lambda: self.buttonPressed(self.L21))
        self.L22.clicked.connect(lambda: self.buttonPressed(self.L22))

        # U side button click events
        self.U00.clicked.connect(lambda: self.buttonPressed(self.U00))
        self.U01.clicked.connect(lambda: self.buttonPressed(self.U01))
        self.U02.clicked.connect(lambda: self.buttonPressed(self.U02))
        self.U10.clicked.connect(lambda: self.buttonPressed(self.U10))
        self.U11.clicked.connect(lambda: self.buttonPressed(self.U11))
        self.U12.clicked.connect(lambda: self.buttonPressed(self.U12))
        self.U20.clicked.connect(lambda: self.buttonPressed(self.U20))
        self.U21.clicked.connect(lambda: self.buttonPressed(self.U21))
        self.U22.clicked.connect(lambda: self.buttonPressed(self.U22))

        # B side button click events
        self.B00.clicked.connect(lambda: self.buttonPressed(self.B00))
        self.B01.clicked.connect(lambda: self.buttonPressed(self.B01))
        self.B02.clicked.connect(lambda: self.buttonPressed(self.B02))
        self.B10.clicked.connect(lambda: self.buttonPressed(self.B10))
        self.B11.clicked.connect(lambda: self.buttonPressed(self.B11))
        self.B12.clicked.connect(lambda: self.buttonPressed(self.B12))
        self.B20.clicked.connect(lambda: self.buttonPressed(self.B20))
        self.B21.clicked.connect(lambda: self.buttonPressed(self.B21))
        self.B22.clicked.connect(lambda: self.buttonPressed(self.B22))

        # F side button click events
        self.F00.clicked.connect(lambda: self.buttonPressed(self.F00))
        self.F01.clicked.connect(lambda: self.buttonPressed(self.F01))
        self.F02.clicked.connect(lambda: self.buttonPressed(self.F02))
        self.F10.clicked.connect(lambda: self.buttonPressed(self.F10))
        self.F11.clicked.connect(lambda: self.buttonPressed(self.F11))
        self.F12.clicked.connect(lambda: self.buttonPressed(self.F12))
        self.F20.clicked.connect(lambda: self.buttonPressed(self.F20))
        self.F21.clicked.connect(lambda: self.buttonPressed(self.F21))
        self.F22.clicked.connect(lambda: self.buttonPressed(self.F22))

        # R side button click events
        self.R00.clicked.connect(lambda: self.buttonPressed(self.R00))
        self.R01.clicked.connect(lambda: self.buttonPressed(self.R01))
        self.R02.clicked.connect(lambda: self.buttonPressed(self.R02))
        self.R10.clicked.connect(lambda: self.buttonPressed(self.R10))
        self.R11.clicked.connect(lambda: self.buttonPressed(self.R11))
        self.R12.clicked.connect(lambda: self.buttonPressed(self.R12))
        self.R20.clicked.connect(lambda: self.buttonPressed(self.R20))
        self.R21.clicked.connect(lambda: self.buttonPressed(self.R21))
        self.R22.clicked.connect(lambda: self.buttonPressed(self.R22))

        # D side button click events
        self.D00.clicked.connect(lambda: self.buttonPressed(self.D00))
        self.D01.clicked.connect(lambda: self.buttonPressed(self.D01))
        self.D02.clicked.connect(lambda: self.buttonPressed(self.D02))
        self.D10.clicked.connect(lambda: self.buttonPressed(self.D10))
        self.D11.clicked.connect(lambda: self.buttonPressed(self.D11))
        self.D12.clicked.connect(lambda: self.buttonPressed(self.D12))
        self.D20.clicked.connect(lambda: self.buttonPressed(self.D20))
        self.D21.clicked.connect(lambda: self.buttonPressed(self.D21))
        self.D22.clicked.connect(lambda: self.buttonPressed(self.D22))

        self.clearButton.clicked.connect(self.clearColors)

        self.submitButton.clicked.connect(self.submitLayout)

        # self.randomButton.clicked.connect(self.randomizeCube)

        self.show()

        # function changes button color of the pressed button based on user input
    def buttonPressed(self, button):
        if self.EditColorBox.currentText() == "Clear Color":
            button.setStyleSheet('background-color: white')
        else:
            if self.colorBox.currentText() == "Red":
                button.setStyleSheet('background-color: red')
            if self.colorBox.currentText() == "Blue":
                button.setStyleSheet('background-color: blue')
            if self.colorBox.currentText() == "White":
                button.setStyleSheet('background-color: white')
            if self.colorBox.currentText() == "Yellow":
                button.setStyleSheet('background-color: yellow')
            if self.colorBox.currentText() == "Orange":
                button.setStyleSheet('background-color: orange')
            if self.colorBox.currentText() == "Green":
                button.setStyleSheet('background-color: green')

    # function clears all color attributes of the board
    def clearColors(self):
        self.L00.setStyleSheet('background-color: none')
        self.L01.setStyleSheet('background-color: none')
        self.L02.setStyleSheet('background-color: none')
        self.L10.setStyleSheet('background-color: none')
        self.L11.setStyleSheet('background-color: none')
        self.L12.setStyleSheet('background-color: none')
        self.L20.setStyleSheet('background-color: none')
        self.L21.setStyleSheet('background-color: none')
        self.L22.setStyleSheet('background-color: none')

        self.U00.setStyleSheet('background-color: none')
        self.U01.setStyleSheet('background-color: none')
        self.U02.setStyleSheet('background-color: none')
        self.U10.setStyleSheet('background-color: none')
        self.U11.setStyleSheet('background-color: none')
        self.U12.setStyleSheet('background-color: none')
        self.U20.setStyleSheet('background-color: none')
        self.U21.setStyleSheet('background-color: none')
        self.U22.setStyleSheet('background-color: none')

        self.R00.setStyleSheet('background-color: none')
        self.R01.setStyleSheet('background-color: none')
        self.R02.setStyleSheet('background-color: none')
        self.R10.setStyleSheet('background-color: none')
        self.R11.setStyleSheet('background-color: none')
        self.R12.setStyleSheet('background-color: none')
        self.R20.setStyleSheet('background-color: none')
        self.R21.setStyleSheet('background-color: none')
        self.R22.setStyleSheet('background-color: none')

        self.D00.setStyleSheet('background-color: none')
        self.D01.setStyleSheet('background-color: none')
        self.D02.setStyleSheet('background-color: none')
        self.D10.setStyleSheet('background-color: none')
        self.D11.setStyleSheet('background-color: none')
        self.D12.setStyleSheet('background-color: none')
        self.D20.setStyleSheet('background-color: none')
        self.D21.setStyleSheet('background-color: none')
        self.D22.setStyleSheet('background-color: none')

        self.B00.setStyleSheet('background-color: none')
        self.B01.setStyleSheet('background-color: none')
        self.B02.setStyleSheet('background-color: none')
        self.B10.setStyleSheet('background-color: none')
        self.B11.setStyleSheet('background-color: none')
        self.B12.setStyleSheet('background-color: none')
        self.B20.setStyleSheet('background-color: none')
        self.B21.setStyleSheet('background-color: none')
        self.B22.setStyleSheet('background-color: none')

        self.F00.setStyleSheet('background-color: none')
        self.F01.setStyleSheet('background-color: none')
        self.F02.setStyleSheet('background-color: none')
        self.F10.setStyleSheet('background-color: none')
        self.F11.setStyleSheet('background-color: none')
        self.F12.setStyleSheet('background-color: none')
        self.F20.setStyleSheet('background-color: none')
        self.F21.setStyleSheet('background-color: none')
        self.F22.setStyleSheet('background-color: none')

    # returns the string color of a button
    def getColor(self, buttonID):
        if buttonID.palette().button().color().name() == "#ff0000":
            return 1
        elif buttonID.palette().button().color().name() == "#ffa500":
            return 4
        elif buttonID.palette().button().color().name() == "#0000ff":
            return 5
        elif buttonID.palette().button().color().name() == "#ffff00":
            return 3
        elif buttonID.palette().button().color().name() == "#008000":
            return 2
        elif buttonID.palette().button().color().name() == "#ffffff":
            return 0
        else:
            return "none"

    # generates the array of colors corresponding to the user's input
    def submitLayout(self):
        # color of each cube element edge
        # GOES IN U, R, F, D, L, B ROW DOMINANT ORDER
        colorsArray = [
            [[self.getColor(self.U00), self.getColor(self.U01), self.getColor(self.U02)],
             [self.getColor(self.U10), self.getColor(self.U11), self.getColor(self.U12)],
             [self.getColor(self.U20), self.getColor(self.U21), self.getColor(self.U22)]],
            [[self.getColor(self.R00), self.getColor(self.R01), self.getColor(self.R02)],
             [self.getColor(self.R10), self.getColor(self.R11), self.getColor(self.R12)],
             [self.getColor(self.R20), self.getColor(self.R21), self.getColor(self.R22)]],
            [[self.getColor(self.F00), self.getColor(self.F01), self.getColor(self.F02)],
             [self.getColor(self.F10), self.getColor(self.F11), self.getColor(self.F12)],
             [self.getColor(self.F20), self.getColor(self.F21), self.getColor(self.F22)]],
            [[self.getColor(self.D00), self.getColor(self.D01), self.getColor(self.D02)],
             [self.getColor(self.D10), self.getColor(self.D11), self.getColor(self.D12)],
             [self.getColor(self.D20), self.getColor(self.D21), self.getColor(self.D22)]],
            [[self.getColor(self.L00), self.getColor(self.L01), self.getColor(self.L02)],
             [self.getColor(self.L10), self.getColor(self.L11), self.getColor(self.L12)],
             [self.getColor(self.L20), self.getColor(self.L21), self.getColor(self.L22)]],
            [[self.getColor(self.B00), self.getColor(self.B01), self.getColor(self.B02)],
             [self.getColor(self.B10), self.getColor(self.B11), self.getColor(self.B12)],
             [self.getColor(self.B20), self.getColor(self.B21), self.getColor(self.B22)]]
        ]

        U = 0
        R = 1
        F = 2
        D = 3
        L = 4
        B = 5

        # sticfrs = [
        # [[R,L,D], [U,U,U], [U,U,U]],
        # [[R,R,B], [L,F,R], [R,R,L]],
        # [[R,L,D], [B,F,F], [D,F,F]],
        # [[U,F,B], [D,R,U], [R,L,F]],
        # [[U,R,F], [U,R,F], [U,B,F]],
        # [[D,R,L], [U,R,F], [D,R,F]]
        # ]

        # stickers = [
        # [[U, L, D], [L, U, D], [D, B, U]],
        # [[R, U, B], [B, R, D], [F, R, U]],
        # [[L, R, L], [D, F, F], [D, R, F]],
        # [[U, B, B], [R, D, D], [R, U, R]],
        # [[D, B, L], [F, L, F], [B, L, F]],
        # [[L, U, R], [L, B, F], [B, U, F]]
        # ]

        stickers = [
        [[U, U, U], [U, U, U], [U, U, U]],
        [[R, R, R], [R, R, R], [R, R, R]],
        [[F, F, F], [F, F, F], [F, F, F]],
        [[D, D, D], [D, D, D], [D, D, D]],
        [[L, L, L], [L, L, L], [L, L, L]],
        [[B, B, B], [B, B, B], [B, B, B]]
        ]

        print(colorsArray)

        cube = to_cube(colorsArray)
        print(cube.BL.piece)

        solution = []  # List of Moves

        solution += solve_DB(cube)
        print(stringify(solution))
        solution += solve_DL(cube)
        print(stringify(solution))
        solution += solve_DR(cube)
        print(stringify(solution))
        solution += solve_DF(cube)
        print(stringify(solution))

        solution += solve_BL_pair(cube)
        print(stringify(solution))
        solution += solve_BR_pair(cube)
        print(stringify(solution))
        solution += solve_FL_pair(cube)
        print(stringify(solution))
        solution += solve_FR_pair(cube)
        print(stringify(solution))

        solution += solve_EO(cube)
        print(stringify(solution))
        solution += solve_CO(cube)
        print(stringify(solution))

        solution += solve_CP_1(cube)
        print(stringify(solution))
        solution += solve_CP_2(cube)
        print(stringify(solution))
        solution += solve_CP_3(cube)
        print(stringify(solution))

        solution += solve_EP_1(cube)
        print(stringify(solution))
        solution += solve_EP_2(cube)
        print(stringify(solution))

        #run the renderer script
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.glWidget = CubeRenderer(colorsArray)
        self.glWidgetArea = QScrollArea()
        self.glWidgetArea.setWidget(self.glWidget)
        self.glWidgetArea.setWidgetResizable(True)

        centralLayout = QGridLayout()
        centralLayout.addWidget(self.glWidgetArea, 0, 0)
        centralWidget.setLayout(centralLayout)

        self.glWidget.solution = solution

        # app.exec_()



app = QApplication([])
mainWin = PyQtWindow()
mainWin.show()
sys.exit(app.exec_())