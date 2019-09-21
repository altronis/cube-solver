import sys
from PyQt5.QtCore import pyqtSignal, Qt, QTimer
from PyQt5.QtWidgets import (QAction, QApplication, QGridLayout, QMainWindow, QMessageBox, QOpenGLWidget, QScrollArea, QSizePolicy, QSlider, QWidget)
import OpenGL.GL as gl
import math
import keyboard


class CubeRenderer(QOpenGLWidget):

    U = 0
    R = 1
    F = 2
    D = 3
    L = 4
    B = 5
    Ui = 6
    Ri = 7
    Fi = 8
    Di = 9
    Li = 10
    Bi = 11

    def __init__(self, stickers):
        super(CubeRenderer, self).__init__(parent=None)

        self.stickers = stickers

        self.xRot = 0
        self.yRot = 0
        self.zRot = 0

        self.reset(self.stickers)

        timer = QTimer(self)
        timer.timeout.connect(self.updatePosition)
        timer.start(20)

    def reset(self, stickers):
        self.firstPassMove = True
        self.orgTheta = []



        self.currentMove = -1
        self.thetaTotal = 0
        self.moveSpeed = 2.5

        self.cubeRot = []
        self.cubePos = []
        self.cubes = []
        for x in range(3):
            self.cubes.append([])
            self.cubePos.append([])
            self.cubeRot.append([])
            for y in range(3):
                self.cubes[x].append([0]*3)
                self.cubePos[x].append([0]*3)
                self.cubeRot[x].append([0]*3)




        self.cubeColors = self.initCubeColors(stickers)


    def initCubeColors(self, stickers):

        colors = []
        for x in range(3):
            colors.append([])
            for y in range(3):
                colors[x].append([])
                for z in range(3):
                    colors[x][y].append([])
                    for _ in range(6):
                        colors[x][y][z].append((0,0,0)) #black

        colors[0][2][0][CubeRenderer.U] = self.getColorTuple(stickers[CubeRenderer.U][0][0]);
        colors[1][2][0][CubeRenderer.U] = self.getColorTuple(stickers[CubeRenderer.U][0][1]);
        colors[2][2][0][CubeRenderer.U] = self.getColorTuple(stickers[CubeRenderer.U][0][2]);

        colors[0][2][1][CubeRenderer.U] = self.getColorTuple(stickers[CubeRenderer.U][1][0]);
        colors[1][2][1][CubeRenderer.U] = self.getColorTuple(stickers[CubeRenderer.U][1][1]);
        colors[2][2][1][CubeRenderer.U] = self.getColorTuple(stickers[CubeRenderer.U][1][2]);

        colors[0][2][2][CubeRenderer.U] = self.getColorTuple(stickers[CubeRenderer.U][2][0]);
        colors[1][2][2][CubeRenderer.U] = self.getColorTuple(stickers[CubeRenderer.U][2][1]);
        colors[2][2][2][CubeRenderer.U] = self.getColorTuple(stickers[CubeRenderer.U][2][2]);

        for y in range(2, -1, -1):
            for z in range(3):
                colors[2][y][z][CubeRenderer.R] = self.getColorTuple(stickers[CubeRenderer.R][z][2-y]);

        for y in range(2, -1, -1):
            for x in range(3):
                colors[x][2-y][2][CubeRenderer.F] = self.getColorTuple(stickers[CubeRenderer.F][y][x]);

        colors[2][0][0][CubeRenderer.D] = self.getColorTuple(stickers[CubeRenderer.D][0][0]);
        colors[1][0][0][CubeRenderer.D] = self.getColorTuple(stickers[CubeRenderer.D][0][1]);
        colors[0][0][0][CubeRenderer.D] = self.getColorTuple(stickers[CubeRenderer.D][0][2]);
        colors[2][0][1][CubeRenderer.D] = self.getColorTuple(stickers[CubeRenderer.D][1][0]);
        colors[1][0][1][CubeRenderer.D] = self.getColorTuple(stickers[CubeRenderer.D][1][1]);
        colors[0][0][1][CubeRenderer.D] = self.getColorTuple(stickers[CubeRenderer.D][1][2]);
        colors[2][0][2][CubeRenderer.D] = self.getColorTuple(stickers[CubeRenderer.D][2][0]);
        colors[1][0][2][CubeRenderer.D] = self.getColorTuple(stickers[CubeRenderer.D][2][1]);
        colors[0][0][2][CubeRenderer.D] = self.getColorTuple(stickers[CubeRenderer.D][2][2]);

        colors[0][0][0][CubeRenderer.L] = self.getColorTuple(stickers[CubeRenderer.L][0][0]);
        colors[0][1][0][CubeRenderer.L] = self.getColorTuple(stickers[CubeRenderer.L][0][1]);
        colors[0][2][0][CubeRenderer.L] = self.getColorTuple(stickers[CubeRenderer.L][0][2]);
        colors[0][0][1][CubeRenderer.L] = self.getColorTuple(stickers[CubeRenderer.L][1][0]);
        colors[0][1][1][CubeRenderer.L] = self.getColorTuple(stickers[CubeRenderer.L][1][1]);
        colors[0][2][1][CubeRenderer.L] = self.getColorTuple(stickers[CubeRenderer.L][1][2]);
        colors[0][0][2][CubeRenderer.L] = self.getColorTuple(stickers[CubeRenderer.L][2][0]);
        colors[0][1][2][CubeRenderer.L] = self.getColorTuple(stickers[CubeRenderer.L][2][1]);
        colors[0][2][2][CubeRenderer.L] = self.getColorTuple(stickers[CubeRenderer.L][2][2]);

        colors[0][0][0][CubeRenderer.B] = self.getColorTuple(stickers[CubeRenderer.B][0][0]);
        colors[1][0][0][CubeRenderer.B] = self.getColorTuple(stickers[CubeRenderer.B][0][1]);
        colors[2][0][0][CubeRenderer.B] = self.getColorTuple(stickers[CubeRenderer.B][0][2]);
        colors[0][1][0][CubeRenderer.B] = self.getColorTuple(stickers[CubeRenderer.B][1][0]);
        colors[1][1][0][CubeRenderer.B] = self.getColorTuple(stickers[CubeRenderer.B][1][1]);
        colors[2][1][0][CubeRenderer.B] = self.getColorTuple(stickers[CubeRenderer.B][1][2]);
        colors[0][2][0][CubeRenderer.B] = self.getColorTuple(stickers[CubeRenderer.B][2][0]);
        colors[1][2][0][CubeRenderer.B] = self.getColorTuple(stickers[CubeRenderer.B][2][1]);
        colors[2][2][0][CubeRenderer.B] = self.getColorTuple(stickers[CubeRenderer.B][2][2]);

        return colors



    def getColorTuple(self, face):
        if(face == CubeRenderer.U):
            return (255/255, 255/255, 255/255)#white
        elif(face == CubeRenderer.R):
            return (178/255, 34/255, 34/255)#red
        elif(face == CubeRenderer.F):
            return (0, 255/255, 0)#green
        elif(face == CubeRenderer.D):
            return (255/255, 255/255, 0)#yellow
        elif(face == CubeRenderer.L):
            return (255/255, 103/255, 0)#orange
        elif(face == CubeRenderer.B):
            return (0, 0, 255/255)#blue

        return (0,0,0)

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

        for x in range(-1, 2):
            for y in range(-1, 2):
                 for z in range(-1, 2):
                    # self.cubes.append(self.makeCube(x*1.1, y*1.1, z*1.1, 1, self.cubeColors[x+1][y+1][z+1]))
                    self.cubePos[x+1][y+1][z+1] = (x*1.1, y*1.1, z*1.1)
                    self.cubeRot[x+1][y+1][z+1] = (0.0, 0,0, 0,0, 0.0, 1.0, 0.0)
                    self.cubes[x+1][y+1][z+1] = self.makeCube(x*1.1, y*1.1, z*1.1, 0.5, self.cubeColors[x+1][y+1][z+1])

        gl.glEnable(gl.GL_NORMALIZE)
        gl.glEnable(gl.GL_DEPTH_TEST);  
        gl.glClearColor(0.5, 0.5, 0.5, 1.0)


    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        gl.glPushMatrix()
        gl.glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
        gl.glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
        gl.glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)
        # gl.glPopMatrix()
        
        # self.drawCube(cube, 0.0, 0.0, 0.0, self.cube1Rot / 16.0)

        # for cube in self.cubes:
        #     self.drawCube(cube, 0.0, 0.0, 0.0, 0 / 16.0)
                                #dx,  dy,  dz, angle
        # gl.glPushMatrix()

        for x in range(3):
            for y in range(3):
                for z in range(3):
                    pos = self.cubePos[x][y][z]
                    rot = self.cubeRot[x][y][z]
                    self.drawCube(self.cubes[x][y][z], pos[0], pos[1], pos[2], rot[0], rot[1], rot[2])

        gl.glPopMatrix()

    def resizeGL(self, width, height):
        side = min(width, height)
        if side < 0:
            return

        gl.glViewport((width - side) // 2, (height - side) // 2, side, side)


        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glFrustum(-1.0, +1.0, -1.0, 1.0, 5.0, 60.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()
        gl.glTranslated(0.0, 0.0, -40.0)
        

    def mousePressEvent(self, event):
        self.lastPos = event.pos()

        if(self.currentMove == -1):
            if keyboard.is_pressed('u'):
                self.currentMove = CubeRenderer.U;
            if keyboard.is_pressed('r'):
                self.currentMove = CubeRenderer.R;
        else:
            print(self.currentMove, self.thetaTotal)



    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()

        if event.buttons() & Qt.LeftButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setYRotation(self.yRot + 8 * dx)

        self.lastPos = event.pos()

    # def advanceGears(self):
    #     # self.gear1Rot += 2 * 16
    #     self.update()

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
        # size /= 2;

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
        # gl.glColor3f(1.0,0.0,1.0)
        tup = colors[2];
        gl.glColor3f(tup[0], tup[1], tup[2])        
        gl.glBegin(gl.GL_QUAD_STRIP)
        gl.glVertex3d(x-size, y-size, z+size)
        gl.glVertex3d(x-size, y+size, z+size)
        gl.glVertex3d(x+size, y-size, z+size)
        gl.glVertex3d(x+size, y+size, z+size)
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
        gl.glColor3f(0.0,1.0,1.0)
        tup = colors[5];
        gl.glColor3f(tup[0], tup[1], tup[2])
        gl.glBegin(gl.GL_QUAD_STRIP)
        gl.glVertex3d(x-size, y-size, z-size)
        gl.glVertex3d(x-size, y+size, z-size)
        gl.glVertex3d(x+size, y-size, z-size)
        gl.glVertex3d(x+size, y+size, z-size)
        gl.glEnd()

        gl.glEndList()

        return list
    first = 0
    def drawCube(self, cube, dx, dy, dz, angleX, angleY, angleZ):
        gl.glPushMatrix()
        # gl.glLoadIdentity()        
        # gl.glTranslated(dx, dy, dz-40.0)
        # gl.glRotated(angle, vx, vy, vz)
        gl.glRotated(angleX, 1, 0, 0)
        gl.glRotated(angleY, 0, 1, 0)
        gl.glRotated(angleZ, 0, 0, 1)

        if CubeRenderer.first <3*3*3:
            CubeRenderer.first+=1
            gl.glTranslated(dx, dy, dz)

        # gl.glRotated(angle, vx, vy, vz)
        gl.glCallList(cube)
        gl.glPopMatrix()

    def normalizeAngle(self, angle):
        while (angle < 0):
            angle += 360
        while (angle > 360):
            angle -= 360
        return angle


    # def rotate(self, origin, point, theta):

    #     ox, oy = origin
    #     px, py = point

    #     qx = ox + math.cos(theta) * (px - ox) - math.sin(theta) * (py - oy)
    #     qy = oy + math.sin(theta) * (px - ox) + math.cos(theta) * (py - oy)
    #     return qx, qy


    def rotate_point(self, cx, cy, angle, px, py):
      s = math.sin(angle);
      c = math.cos(angle);

      # translate point back to origin:
      px -= cx;
      py -= cy;

      # // rotate point
      xnew = px * c - py * s;
      ynew = px * s + py * c;

      # // translate point back:
      px = xnew + cx;
      py = ynew + cy;
      return (px, py);


    def updatePosition(self):
        # print(self.currentMove)
        if self.currentMove == CubeRenderer.U:
            self.moveU()
        elif self.currentMove == CubeRenderer.R:
            self.moveR()
        elif self.currentMove == CubeRenderer.F:
            pass
        elif self.currentMove == CubeRenderer.D:
            pass
        elif self.currentMove == CubeRenderer.L:
            pass
        elif self.currentMove == CubeRenderer.B:
            pass
        else:
            return

        if(self.currentMove == -1):
            self.thetaTotal = 0
        reset()
        # self.update()


    def swap4Cubes(self, ind1, ind2, ind3, ind4):
        # print(id(self.cubes[ind1[0]][ind1[1]][ind1[2]]))
        # print(id(self.cubes[ind2[0]][ind2[1]][ind2[2]]))
        # print(id(self.cubes[ind3[0]][ind3[1]][ind3[2]]))
        # print(id(self.cubes[ind4[0]][ind4[1]][ind4[2]]))
        # print()

        temp = self.cubes[ind1[0]][ind1[1]][ind1[2]]
        self.cubes[ind1[0]][ind1[1]][ind1[2]] = self.cubes[ind4[0]][ind4[1]][ind4[2]]
        self.cubes[ind4[0]][ind4[1]][ind4[2]] = self.cubes[ind3[0]][ind3[1]][ind3[2]]
        self.cubes[ind3[0]][ind3[1]][ind3[2]] = self.cubes[ind2[0]][ind2[1]][ind2[2]]
        self.cubes[ind2[0]][ind2[1]][ind2[2]] = temp

        # print(id(self.cubes[ind1[0]][ind1[1]][ind1[2]]))
        # print(id(self.cubes[ind2[0]][ind2[1]][ind2[2]]))
        # print(id(self.cubes[ind3[0]][ind3[1]][ind3[2]]))
        # print(id(self.cubes[ind4[0]][ind4[1]][ind4[2]]))

        temp = self.cubeRot[ind1[0]][ind1[1]][ind1[2]]
        self.cubeRot[ind1[0]][ind1[1]][ind1[2]] = self.cubeRot[ind4[0]][ind4[1]][ind4[2]]
        self.cubeRot[ind4[0]][ind4[1]][ind4[2]] = self.cubeRot[ind3[0]][ind3[1]][ind3[2]]
        self.cubeRot[ind3[0]][ind3[1]][ind3[2]] = self.cubeRot[ind2[0]][ind2[1]][ind2[2]]
        self.cubeRot[ind2[0]][ind2[1]][ind2[2]] = temp

        temp = self.cubePos[ind1[0]][ind1[1]][ind1[2]]
        self.cubePos[ind1[0]][ind1[1]][ind1[2]] = self.cubePos[ind4[0]][ind4[1]][ind4[2]]
        self.cubePos[ind4[0]][ind4[1]][ind4[2]] = self.cubePos[ind3[0]][ind3[1]][ind3[2]]
        self.cubePos[ind3[0]][ind3[1]][ind3[2]] = self.cubePos[ind2[0]][ind2[1]][ind2[2]]
        self.cubePos[ind2[0]][ind2[1]][ind2[2]] = temp




    def moveU(self):
        self.thetaTotal += self.moveSpeed
        
        if(self.firstPassMove):
            self.firstPassMove = False

            for x in range(3):
                for z in range(3):
                    self.orgTheta.append((self.cubeRot[x][2][z][0], self.cubeRot[x][2][z][1], self.cubeRot[x][2][z][2]))

        for x in range(3):
            for z in range(3):
                self.cubeRot[x][2][z] = (self.orgTheta[z+3*x][0], self.orgTheta[z+3*x][1] - self.thetaTotal, self.orgTheta[z+3*x][2], 0, -1.0, 0)
                # self.cubeRot[x][2][z] = (self.thetaTotal, 0, -1.0, 0)


        if(self.thetaTotal >= 90):
            self.currentMove = -1
            self.firstPassMove = True
            self.orgTheta = []
            # print(self.cubePos[2][2][2])

            self.swap4Cubes((0,2,0),(2,2,0),(2,2,2),(0,2,2)) #in directions
            # self.swap4Cubes((0,2,0),(2,2,0),(2,2,2),(0,2,2))
            # self.swap4Cubes((0,2,0),(2,2,0),(2,2,2),(0,2,2))
            # self.swap4Cubes((0,2,1),(1,2,0),(2,2,1),(1,2,2))
            # self.swap4Cubes((0,2,2),(2,2,2),(2,2,0),(0,2,0))

            # print(self.cubePos[2][2][2])




    def moveR(self):
        self.thetaTotal += self.moveSpeed
        
        if(self.firstPassMove):
            self.firstPassMove = False

            for y in range(3):
                for z in range(3):
                    # self.orgTheta.append(self.cubeRot[2][y][z][0])
                    self.orgTheta.append((self.cubeRot[2][y][z][0], self.cubeRot[2][y][z][1], self.cubeRot[2][y][z][2]))

        for y in range(3):
            for z in range(3):
                # self.cubeRot[2][y][z] = (self.orgTheta[z+3*y] + self.thetaTotal, -1.0, 0, 0)
                self.cubeRot[2][y][z] = (self.orgTheta[z+3*y][0] - self.thetaTotal, self.orgTheta[z+3*y][1], self.orgTheta[z+3*y][2], -1.0, 0.0, 0)

        if(self.thetaTotal >= 90):
            self.currentMove = -1
            self.firstPassMove = True
            self.orgTheta = []
            self.swap4Cubes((2,2,2),(2,2,0),(2,0,0),(2,0,2))#in direction




