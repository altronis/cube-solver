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

        stickers = [
        [[U,U,U], [U,U,U], [U,U,U]],
        [[R,R,R], [R,R,R], [R,R,R]],
        [[F,F,F], [F,F,F], [F,F,F]],
        [[D,D,D], [D,D,D], [D,D,D]],
        [[L,L,L], [L,L,L], [L,L,L]],
        [[B,B,B], [B,B,B], [B,B,B]]
        ];

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