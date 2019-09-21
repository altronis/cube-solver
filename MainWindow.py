from PyQt5.QtWidgets import (QAction, QApplication, QGridLayout, QMainWindow, QScrollArea, QSizePolicy, QSlider, QWidget)
from CubeRenderer import CubeRenderer
from PyQt5.QtCore import Qt
import sys

# URFDLB

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

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




        self.glWidget = CubeRenderer(stickers)

        self.glWidgetArea = QScrollArea()
        self.glWidgetArea.setWidget(self.glWidget)
        self.glWidgetArea.setWidgetResizable(True)
        self.glWidgetArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.glWidgetArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.glWidgetArea.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.glWidgetArea.setMinimumSize(50, 50)

        centralLayout = QGridLayout()
        centralLayout.addWidget(self.glWidgetArea, 0, 0)
        centralWidget.setLayout(centralLayout)

        self.setWindowTitle("Cube Solver")
        self.resize(600, 600)
        self.setFixedSize(600, 600)




if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())