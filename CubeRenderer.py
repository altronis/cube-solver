import sys
from PyQt5.QtCore import pyqtSignal, Qt, QTimer
from PyQt5.QtWidgets import (QAction, QApplication, QGridLayout, QMainWindow, QMessageBox, QOpenGLWidget, QScrollArea, QSizePolicy, QSlider, QWidget)
import OpenGL.GL as gl


class CubeRenderer(QOpenGLWidget):

    def __init__(self, stickers):
        super(CubeRenderer, self).__init__(parent=None)

        self.xRot = 0
        self.yRot = 0
        self.zRot = 0

        self.cubes = []

        self.cubeColors = [[[[]]*3]*3]*3

        print(len(self.cubeColors))
        print(len(self.cubeColors[0]))
        print(len(self.cubeColors[0][0]))
        print(len(self.cubeColors[0][0][0]))

        self.initCubeColors(stickers)


        timer = QTimer(self)
        timer.timeout.connect(self.advanceGears)
        timer.start(20)

    def initCubeColors(self, stickers):
        for x in range(len(self.cubeColors)):
            for y in range(len(self.cubeColors[x])):
                for z in range(len(self.cubeColors[x][y])):
                    for _ in range(6):
                        self.cubeColors[x][y][z].append((0.0,0.0,0.0)) #black

        

    def setXRotation(self, angle):
        # self.normalizeAngle(angle)

        if angle != self.xRot:
            self.xRot = angle
            self.update()


    def setYRotation(self, angle):
        # self.normalizeAngle(angle)

        if angle != self.yRot:
            self.yRot = angle
            self.update()


    def setZRotation(self, angle):
        # self.normalizeAngle(angle)

        if angle != self.zRot:
            self.zRot = angle
            self.update()


    def initializeGL(self):

        # print(len(self.cubeColors))
        # print(len(self.cubeColors[0]))
        # print(len(self.cubeColors[0][0]))
        # print(len(self.cubeColors[0][0][0]))


        for x in range(-1, 2):
            for y in range(-1, 2):
                 for z in range(-1, 2):
                    self.cubes.append(self.makeCube(x*1.1, y*1.1, z*1.1, 1, self.cubeColors[x+1][y+1][z+1]))

        gl.glEnable(gl.GL_NORMALIZE)
        gl.glEnable(gl.GL_DEPTH_TEST);  
        gl.glClearColor(0.5, 0.5, 0.5, 1.0)


    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        gl.glPushMatrix()
        gl.glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
        gl.glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
        gl.glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)

        
        # self.drawCube(cube, 0.0, 0.0, 0.0, self.cube1Rot / 16.0)
        for cube in self.cubes:
            self.drawCube(cube, 0.0, 0.0, 0.0, 0 / 16.0)
                                #dx,  dy,  dz, angle

        gl.glPopMatrix()

    def resizeGL(self, width, height):
        side = min(width, height)
        if side < 0:
            return

        gl.glViewport((width - side) // 2, (height - side) // 2, side, side)


        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glFrustum(-1.0, +1.0, -1.0, 1.0, 5.0, 60.0)
        # gl.glOrtho(-5.0, +5.0, -5.0, 5.0, 0.0, 100.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()
        gl.glTranslated(0.0, 0.0, -40.0)
        

    def mousePressEvent(self, event):
        self.lastPos = event.pos()

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()

        if event.buttons() & Qt.LeftButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setYRotation(self.yRot + 8 * dx)

        self.lastPos = event.pos()

    def advanceGears(self):
        # self.gear1Rot += 2 * 16
        self.update()

    def xRotation(self):
        return self.xRot

    def yRotation(self):
        return self.yRot

    def zRotation(self):
        return self.zRot
    
    # URFDLB
    def makeCube(self, x, y, z, size, colors):
        list = gl.glGenLists(1)
        gl.glNewList(list, gl.GL_COMPILE)
        size /= 2;

        # up face
        # gl.glColor3f(0.0,0.0,1.0)
        tup = colors[0];
        gl.glColor3f(tup[0], tup[1], tup[2])
        gl.glBegin(gl.GL_QUAD_STRIP)
        gl.glVertex3d(x+size, y+size, z-size)
        gl.glVertex3d(x+size, y+size, z+size)
        gl.glVertex3d(x-size, y+size, z-size)
        gl.glVertex3d(x-size, y+size, z+size)
        gl.glEnd()

        # right face
        # gl.glColor3f(0.0,1.0,0.0)
        tup = colors[1];
        gl.glColor3f(tup[0], tup[1], tup[2])
        gl.glBegin(gl.GL_QUADS)
        gl.glVertex3d(x+size, y-size, z-size)
        gl.glVertex3d(x+size, y-size, z+size)
        gl.glVertex3d(x+size, y+size, z+size)
        gl.glVertex3d(x+size, y+size, z-size)
        gl.glEnd()

        # front face
        # gl.glColor3f(0.0,1.0,1.0)
        tup = colors[2];
        gl.glColor3f(tup[0], tup[1], tup[2])
        gl.glBegin(gl.GL_QUAD_STRIP)
        gl.glVertex3d(x-size, y-size, z-size)
        gl.glVertex3d(x-size, y+size, z-size)
        gl.glVertex3d(x+size, y-size, z-size)
        gl.glVertex3d(x+size, y+size, z-size)
        gl.glEnd()

        # down face
        # gl.glColor3f(1.0,0.0,0.0)
        tup = colors[3];
        gl.glColor3f(tup[0], tup[1], tup[2])
        gl.glBegin(gl.GL_QUADS)        
        gl.glVertex3d(x-size, y-size, z-size)
        gl.glVertex3d(x+size, y-size, z-size)
        gl.glVertex3d(x+size, y-size,  z+size)
        gl.glVertex3d(x-size, y-size,  z+size)
        gl.glEnd()

        # left face
        # gl.glColor3f(1.0,1.0,0.0)
        tup = colors[4];
        gl.glColor3f(tup[0], tup[1], tup[2])
        gl.glBegin(gl.GL_QUAD_STRIP)
        gl.glVertex3d(x-size, y+size, z-size)
        gl.glVertex3d(x-size, y+size, z+size)
        gl.glVertex3d(x-size, y-size, z-size)
        gl.glVertex3d(x-size, y-size, z+size)
        gl.glEnd()

        # back face
        # gl.glColor3f(1.0,0.0,1.0)
        tup = colors[5];
        gl.glColor3f(tup[0], tup[1], tup[2])        
        gl.glBegin(gl.GL_QUAD_STRIP)
        gl.glVertex3d(x-size, y-size, z+size)
        gl.glVertex3d(x-size, y+size, z+size)
        gl.glVertex3d(x+size, y-size, z+size)
        gl.glVertex3d(x+size, y+size, z+size)
        gl.glEnd()

        gl.glEndList()

        return list

    def drawCube(self, cube, dx, dy, dz, angle):
        gl.glPushMatrix()
        gl.glTranslated(dx, dy, dz)
        gl.glRotated(angle, 0.0, 0.0, 1.0)
        gl.glCallList(cube)
        gl.glPopMatrix()

    def normalizeAngle(self, angle):
        while (angle < 0):
            angle += 360
        while (angle > 360):
            angle -= 360
        return angle