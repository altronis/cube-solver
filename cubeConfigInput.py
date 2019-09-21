from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import random

class PyQtWindow(QMainWindow):
    def __init__(self):
        app = QApplication([])
        super().__init__()

        uic.loadUi("CubeConfigLayout.ui", self)

        # dropdown options for color combo
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
        self.L00.clicked.connect(lambda: buttonPressed(self.L00))
        self.L01.clicked.connect(lambda: buttonPressed(self.L01))
        self.L02.clicked.connect(lambda: buttonPressed(self.L02))
        self.L10.clicked.connect(lambda: buttonPressed(self.L10))
        self.L11.clicked.connect(lambda: buttonPressed(self.L11))
        self.L12.clicked.connect(lambda: buttonPressed(self.L12))
        self.L20.clicked.connect(lambda: buttonPressed(self.L20))
        self.L21.clicked.connect(lambda: buttonPressed(self.L21))
        self.L22.clicked.connect(lambda: buttonPressed(self.L22))

        # U side button click events
        self.U00.clicked.connect(lambda: buttonPressed(self.U00))
        self.U01.clicked.connect(lambda: buttonPressed(self.U01))
        self.U02.clicked.connect(lambda: buttonPressed(self.U02))
        self.U10.clicked.connect(lambda: buttonPressed(self.U10))
        self.U11.clicked.connect(lambda: buttonPressed(self.U11))
        self.U12.clicked.connect(lambda: buttonPressed(self.U12))
        self.U20.clicked.connect(lambda: buttonPressed(self.U20))
        self.U21.clicked.connect(lambda: buttonPressed(self.U21))
        self.U22.clicked.connect(lambda: buttonPressed(self.U22))

        # B side button click events
        self.B00.clicked.connect(lambda: buttonPressed(self.B00))
        self.B01.clicked.connect(lambda: buttonPressed(self.B01))
        self.B02.clicked.connect(lambda: buttonPressed(self.B02))
        self.B10.clicked.connect(lambda: buttonPressed(self.B10))
        self.B11.clicked.connect(lambda: buttonPressed(self.B11))
        self.B12.clicked.connect(lambda: buttonPressed(self.B12))
        self.B20.clicked.connect(lambda: buttonPressed(self.B20))
        self.B21.clicked.connect(lambda: buttonPressed(self.B21))
        self.B22.clicked.connect(lambda: buttonPressed(self.B22))

        # F side button click events
        self.F00.clicked.connect(lambda: buttonPressed(self.F00))
        self.F01.clicked.connect(lambda: buttonPressed(self.F01))
        self.F02.clicked.connect(lambda: buttonPressed(self.F02))
        self.F10.clicked.connect(lambda: buttonPressed(self.F10))
        self.F11.clicked.connect(lambda: buttonPressed(self.F11))
        self.F12.clicked.connect(lambda: buttonPressed(self.F12))
        self.F20.clicked.connect(lambda: buttonPressed(self.F20))
        self.F21.clicked.connect(lambda: buttonPressed(self.F21))
        self.F22.clicked.connect(lambda: buttonPressed(self.F22))

        # R side button click events
        self.R00.clicked.connect(lambda: buttonPressed(self.R00))
        self.R01.clicked.connect(lambda: buttonPressed(self.R01))
        self.R02.clicked.connect(lambda: buttonPressed(self.R02))
        self.R10.clicked.connect(lambda: buttonPressed(self.R10))
        self.R11.clicked.connect(lambda: buttonPressed(self.R11))
        self.R12.clicked.connect(lambda: buttonPressed(self.R12))
        self.R20.clicked.connect(lambda: buttonPressed(self.R20))
        self.R21.clicked.connect(lambda: buttonPressed(self.R21))
        self.R22.clicked.connect(lambda: buttonPressed(self.R22))

        # D side button click events
        self.D00.clicked.connect(lambda: buttonPressed(self.D00))
        self.D01.clicked.connect(lambda: buttonPressed(self.D01))
        self.D02.clicked.connect(lambda: buttonPressed(self.D02))
        self.D10.clicked.connect(lambda: buttonPressed(self.D10))
        self.D11.clicked.connect(lambda: buttonPressed(self.D11))
        self.D12.clicked.connect(lambda: buttonPressed(self.D12))
        self.D20.clicked.connect(lambda: buttonPressed(self.D20))
        self.D21.clicked.connect(lambda: buttonPressed(self.D21))
        self.D22.clicked.connect(lambda: buttonPressed(self.D22))

        self.clearButton.clicked.connect(lambda: clearColors())

        self.submitButton.clicked.connect(lambda: submitLayout())

        self.randomButton.clicked.connect(lambda: randomizeCube())

        self.show()

        # function changes button color of the pressed button based on user input
        def buttonPressed(button):
            if self.EditColorBox.currentText() == "Clear Color":
                button.setStyleSheet('background-color: none')
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
        def clearColors():
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
        def getColor(buttonID):
            if buttonID.palette().button().color().name() == "#ff0000":
                return "red"
            elif buttonID.palette().button().color().name() == "#ffa500":
                return "orange"
            elif buttonID.palette().button().color().name() == "#0000ff":
                return "blue"
            elif buttonID.palette().button().color().name() == "#ffff00":
                return "yellow"
            elif buttonID.palette().button().color().name() == "#008000":
                return "green"
            elif buttonID.palette().button().color().name() == "#ffffff":
                return "white"
            else:
                return "none"
        # generates the array of colors corresponding to the user's input
        def submitLayout():
            # color of each cube element edge
            # GOES IN U, R, F, D, L, B ROW DOMINANT ORDER
            colorsArray = [
            [[getColor(self.U00), getColor(self.U01), getColor(self.U02)],
             [getColor(self.U10), getColor(self.U11), getColor(self.U12)],
             [getColor(self.U20), getColor(self.U21), getColor(self.U22)]],
            [[getColor(self.R00), getColor(self.R01), getColor(self.R02)],
             [getColor(self.R10), getColor(self.R11), getColor(self.R12)],
             [getColor(self.R20), getColor(self.R21), getColor(self.R22)]],
            [[getColor(self.F00), getColor(self.F01), getColor(self.F02)],
             [getColor(self.F10), getColor(self.F11), getColor(self.F12)],
             [getColor(self.F20), getColor(self.F21), getColor(self.F22)]],
            [[getColor(self.D00), getColor(self.D01), getColor(self.D02)],
             [getColor(self.D10), getColor(self.D11), getColor(self.D12)],
             [getColor(self.D20), getColor(self.D21), getColor(self.D22)]],
            [[getColor(self.L00), getColor(self.L01), getColor(self.L02)],
             [getColor(self.L10), getColor(self.L11), getColor(self.L12)],
             [getColor(self.L20), getColor(self.L21), getColor(self.L22)]],
            [[getColor(self.B00), getColor(self.B01), getColor(self.B02)],
             [getColor(self.B10), getColor(self.B11), getColor(self.B12)],
             [getColor(self.B20), getColor(self.B21), getColor(self.B22)]]
            ]
            return colorsArray

        def randomizeCube():
            colors = ["red", "orange", "yellow", "blue", "green", "white"]
            self.L00.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.L01.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.L02.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.L10.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.L11.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.L12.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.L20.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.L21.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.L22.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])

            self.U00.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.U01.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.U02.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.U10.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.U11.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.U12.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.U20.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.U21.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.U22.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])

            self.R00.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.R01.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.R02.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.R10.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.R11.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.R12.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.R20.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.R21.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.R22.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])

            self.D00.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.D01.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.D02.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.D10.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.D11.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.D12.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.D20.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.D21.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.D22.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])

            self.B00.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.B01.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.B02.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.B10.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.B11.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.B12.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.B20.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.B21.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.B22.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])

            self.F00.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.F01.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.F02.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.F10.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.F11.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.F12.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.F20.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.F21.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])
            self.F22.setStyleSheet('background-color: ' + colors[random.randint(0, 5)])


        app.exec_()

PyQtWindow()
