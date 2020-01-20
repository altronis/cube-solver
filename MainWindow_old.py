from PyQt5.QtWidgets import (QAction, QApplication, QGridLayout, QMainWindow, QScrollArea, QSizePolicy, QSlider, QWidget)
from CubeRenderer import CubeRenderer
from PyQt5.QtCore import Qt
import sys
import keyboard


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

        centralLayout = QGridLayout()
        centralLayout.addWidget(self.glWidgetArea, 0, 0)
        centralWidget.setLayout(centralLayout)

        self.setWindowTitle("Cube Solver")
        self.resize(600, 600)
        self.setFixedSize(600, 600)

    def keyPressEvent(self, e):
        shift = keyboard.is_pressed('shift')

        if (self.glWidget.currentMove == -1):
            if e.key() == Qt.Key_U:
                if shift:
                    self.glWidget.currentMove = CubeRenderer.Ui
                else:
                    self.glWidget.currentMove = CubeRenderer.U
            if e.key() == Qt.Key_D:
                if shift:
                    self.glWidget.currentMove = CubeRenderer.Di
                else:
                    self.glWidget.currentMove = CubeRenderer.D
            if e.key() == Qt.Key_L:
                if shift:
                    self.glWidget.currentMove = CubeRenderer.Li
                else:
                    self.glWidget.currentMove = CubeRenderer.L
            if e.key() == Qt.Key_R:
                if shift:
                    self.glWidget.currentMove = CubeRenderer.Ri
                else:
                    self.glWidget.currentMove = CubeRenderer.R
            if e.key() == Qt.Key_F:
                if shift:
                    self.glWidget.currentMove = CubeRenderer.Fi
                else:
                    self.glWidget.currentMove = CubeRenderer.F
            if e.key() == Qt.Key_B:
                if shift:
                    self.glWidget.currentMove = CubeRenderer.Bi
                else:
                    self.glWidget.currentMove = CubeRenderer.B


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
