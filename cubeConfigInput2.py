from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class PyQtWindow(QMainWindow):
    def __init__(self):
        app = QApplication([])
        super().__init__()

        uic.loadUi("CubeConfigLayout.ui", self)

        # L side button click events
        self.L00.clicked.connect(self.buttonPressed(self.L00))
        self.L01.clicked.connect(self.buttonPressed(self.L01))
        self.L02.clicked.connect(self.buttonPressed(self.L02))
        self.L10.clicked.connect(self.buttonPressed(self.L10))
        self.L11.clicked.connect(self.buttonPressed(self.L11))
        self.L12.clicked.connect(self.buttonPressed(self.L12))
        self.L20.clicked.connect(self.buttonPressed(self.L20))
        self.L21.clicked.connect(self.buttonPressed(self.L21))
        self.L22.clicked.connect(self.buttonPressed(self.L22))

        # U side button click events
        self.U00.clicked.connect(self.buttonPressed(self.L00))
        self.U01.clicked.connect(self.buttonPressed(self.L01))
        self.U02.clicked.connect(self.buttonPressed(self.L02))
        self.U10.clicked.connect(self.buttonPressed(self.L10))
        self.U11.clicked.connect(self.buttonPressed(self.L11))
        self.U12.clicked.connect(self.buttonPressed(self.L12))
        self.U20.clicked.connect(self.buttonPressed(self.L20))
        self.U21.clicked.connect(self.buttonPressed(self.L21))
        self.U22.clicked.connect(self.buttonPressed(self.L22))

        # B side button click events
        self.B00.clicked.connect(self.buttonPressed(self.L00))
        self.B01.clicked.connect(self.buttonPressed(self.L01))
        self.B02.clicked.connect(self.buttonPressed(self.L02))
        self.B10.clicked.connect(self.buttonPressed(self.L10))
        self.B11.clicked.connect(self.buttonPressed(self.L11))
        self.B12.clicked.connect(self.buttonPressed(self.L12))
        self.B20.clicked.connect(self.buttonPressed(self.L20))
        self.B21.clicked.connect(self.buttonPressed(self.L21))
        self.B22.clicked.connect(self.buttonPressed(self.L22))

        # F side button click events
        self.F00.clicked.connect(self.buttonPressed(self.L00))
        self.F01.clicked.connect(self.buttonPressed(self.L01))
        self.F02.clicked.connect(self.buttonPressed(self.L02))
        self.F10.clicked.connect(self.buttonPressed(self.L10))
        self.F11.clicked.connect(self.buttonPressed(self.L11))
        self.F12.clicked.connect(self.buttonPressed(self.L12))
        self.F20.clicked.connect(self.buttonPressed(self.L20))
        self.F21.clicked.connect(self.buttonPressed(self.L21))
        self.F22.clicked.connect(self.buttonPressed(self.L22))

        # R side button click events
        self.R00.clicked.connect(self.buttonPressed(self.L00))
        self.R01.clicked.connect(self.buttonPressed(self.L01))
        self.R02.clicked.connect(self.buttonPressed(self.L02))
        self.R10.clicked.connect(self.buttonPressed(self.L10))
        self.R11.clicked.connect(self.buttonPressed(self.L11))
        self.R12.clicked.connect(self.buttonPressed(self.L12))
        self.R20.clicked.connect(self.buttonPressed(self.L20))
        self.R21.clicked.connect(self.buttonPressed(self.L21))
        self.R22.clicked.connect(self.buttonPressed(self.L22))

        # D side button click events
        self.D00.clicked.connect(self.buttonPressed(self.L00))
        self.D01.clicked.connect(self.buttonPressed(self.L01))
        self.D02.clicked.connect(self.buttonPressed(self.L02))
        self.D10.clicked.connect(self.buttonPressed(self.L10))
        self.D11.clicked.connect(self.buttonPressed(self.L11))
        self.D12.clicked.connect(self.buttonPressed(self.L12))
        self.D20.clicked.connect(self.buttonPressed(self.L20))
        self.D21.clicked.connect(self.buttonPressed(self.L21))
        self.D22.clicked.connect(self.buttonPressed(self.L22))

        # function changes button color of the pressed button based on user input
        def buttonPressed(buttonID):
            try:
                color = input("Enter a color for this side: ")
                self.buttonID.setStyleSheet("background-color: " + color)
            except:
                print("Invalid color selection")

        self.show()

        app.exec_()


