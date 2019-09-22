from PyQt5.QtWidgets import (QAction, QApplication, QGridLayout, QMainWindow, QScrollArea, QSizePolicy, QSlider, QWidget)
from CubeRenderer import CubeRenderer
from PyQt5.QtCore import Qt
import sys
import keyboard

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

        if e.key()==Qt.Key_U:
            if shift:
                self.glWidget.moveQueue.append(CubeRenderer.Ui)
            else:
                self.glWidget.moveQueue.append(CubeRenderer.U)
        if e.key()==Qt.Key_D:
            if shift:
                self.glWidget.moveQueue.append(CubeRenderer.Di)
            else:
                self.glWidget.moveQueue.append(CubeRenderer.D)
        if e.key()==Qt.Key_L:
            if shift:
                self.glWidget.moveQueue.append(CubeRenderer.Li)
            else:
                self.glWidget.moveQueue.append(CubeRenderer.L)
        if e.key()==Qt.Key_R:
            if shift:
                self.glWidget.moveQueue.append(CubeRenderer.Ri)
            else:
                self.glWidget.moveQueue.append(CubeRenderer.R)
        if e.key()==Qt.Key_F:
            if shift:
                self.glWidget.moveQueue.append(CubeRenderer.Fi)
            else:
                self.glWidget.moveQueue.append(CubeRenderer.F)
        if e.key()==Qt.Key_B:
            if shift:
                self.glWidget.moveQueue.append(CubeRenderer.Bi)
            else:
                self.glWidget.moveQueue.append(CubeRenderer.B)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())