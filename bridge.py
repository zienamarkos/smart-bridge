
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *
import numpy as np


def init():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-3.0, 3.0, -3.0, 3.0)
    glEnable(GL_DEPTH_TEST)


def ocean():
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.4, 0.7)
    glVertex3f(-5.0, -0.415, 5.0)
    glVertex3f(5.0, -0.415, 5.0)
    glVertex3f(5.0, -0.415, -5.0)
    glVertex3f(-5.0, -0.415, -5.0)
    glEnd()


def road():
    i = 0.0
    while i <= 4.0:

        glBegin(GL_QUADS)
        # right
        glColor3f(0.3, 0.3, 0.3)
        glVertex3f(-3.0 + i, -0.4, 0.17)
        glVertex3f(-0.5 + i, -0.4, 0.17)
        glVertex3f(-0.5 + i, -0.25, 0.17)
        glVertex3f(-3.0 + i, -0.25, 0.17)

        glVertex3f(-3.0 + i, -0.4, -0.17)
        glVertex3f(-0.5 + i, -0.4, -0.17)
        glVertex3f(-0.5 + i, -0.25, -0.17)
        glVertex3f(-3.0 + i, -0.25, -0.17)

        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(-3.0 + i, -0.25, 0.17)
        glVertex3f(-0.5 + i, -0.25, 0.17)
        glVertex3f(-0.5 + i, -0.25, -0.17)
        glVertex3f(-3.0 + i, -0.25, -0.17)

        glEnd()
        i += 3.5
        break

        # left
    i = 0.0
    while i <= 4.0:
        glBegin(GL_QUADS)
        glColor3f(0.3, 0.3, 0.3)
        glVertex3f(3.0 + i, -0.4, 0.17)
        glVertex3f(0.5 + i, -0.4, 0.17)
        glVertex3f(0.5 + i, -0.25, 0.17)
        glVertex3f(3.0 + i, -0.25, 0.17)

        glVertex3f(3.0 + i, -0.4, -0.17)
        glVertex3f(0.5 + i, -0.4, -0.17)
        glVertex3f(0.5 + i, -0.25, -0.17)
        glVertex3f(3.0 + i, -0.25, -0.17)

        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(3.0 + i, -0.25, 0.17)
        glVertex3f(0.5 + i, -0.25, 0.17)
        glVertex3f(0.5 + i, -0.25, -0.17)
        glVertex3f(3.0 + i, -0.25, -0.17)

        glEnd()
        i += 3.5
        break


def base():

    i = 0.0
    while i <= 1.0:

        glBegin(GL_QUADS)
        # left side
        glColor3f(0.1,0.1,0.1)  # front
        glVertex3f(-0.5+i,-0.4,0.2)
        glVertex3f(-0.3+i,-0.4,0.2)
        glVertex3f(-0.3+i,-0.25,0.2)
        glVertex3f(-0.5+i,-0.25,0.2)

        glColor3f(0.3,0.3,0.3)  # left
        glVertex3f(-0.5+i,-0.4,0.2)
        glVertex3f(-0.5+i,-0.4,-0.2)
        glVertex3f(-0.5+i,-0.25,-0.2)
        glVertex3f(-0.5+i,-0.25,0.2)

        glColor3f(0.1,0.1,0.1)  # back
        glVertex3f(-0.5+i,-0.4,-0.2)
        glVertex3f(-0.3+i,-0.4,-0.2)
        glVertex3f(-0.3+i,-0.25,-0.2)
        glVertex3f(-0.5+i,-0.25,-0.2)

        glColor3f(0.3,0.3,0.3)  # right
        glVertex3f(-0.3+i,-0.4,0.2)
        glVertex3f(-0.3+i,-0.4,-0.2)
        glVertex3f(-0.3+i,-0.25,-0.2)
        glVertex3f(-0.3+i,-0.25,0.2)

        glColor3f(0.0,0.0,0.0)  # top
        glVertex3f(-0.5+i,-0.25,0.2)
        glVertex3f(-0.3+i,-0.25,0.2)
        glVertex3f(-0.3+i,-0.25,-0.2)
        glVertex3f(-0.5+i,-0.25,-0.2)

        # right side
        glColor3f(0.1, 0.1, 0.1)  # front
        glVertex3f(0.5 + i, -0.4, 0.2)
        glVertex3f(0.3 + i, -0.4, 0.2)
        glVertex3f(0.3 + i, -0.25, 0.2)
        glVertex3f(0.5 + i, -0.25, 0.2)

        glColor3f(0.3, 0.3, 0.3)  # left
        glVertex3f(0.5 + i, -0.4, 0.2)
        glVertex3f(0.5 + i, -0.4, -0.2)
        glVertex3f(0.5 + i, -0.25, -0.2)
        glVertex3f(0.5 + i, -0.25, 0.2)

        glColor3f(0.1, 0.1, 0.1)  # back
        glVertex3f(0.5 + i, -0.4, -0.2)
        glVertex3f(0.3 + i, -0.4, -0.2)
        glVertex3f(0.3 + i, -0.25, -0.2)
        glVertex3f(0.5 + i, -0.25, -0.2)

        glColor3f(0.3, 0.3, 0.3)  # right
        glVertex3f(0.3 + i, -0.4, 0.2)
        glVertex3f(0.3 + i, -0.4, -0.2)
        glVertex3f(0.3 + i, -0.25, -0.2)
        glVertex3f(0.3 + i, -0.25, 0.2)

        glColor3f(0.0, 0.0, 0.0)  # top
        glVertex3f(0.5 + i, -0.25, 0.2)
        glVertex3f(0.3 + i, -0.25, 0.2)
        glVertex3f(0.3 + i, -0.25, -0.2)
        glVertex3f(0.5 + i, -0.25, -0.2)
        glEnd()

        i += 0.8
        break


def line():

    glBegin(GL_LINES)
    glColor3f(1.0,1.0,1.0)
    # //left
    glVertex3f(-3.0,-0.23,0.0)
    glVertex3f(-0.3,-0.23,0.0)
    # //right

    glVertex3f(3.0,-0.23,0.0)
    glVertex3f(0.3,-0.23,0.0)
    glEnd()


def bridge():
    glBegin(GL_QUADS)
    # bridge floor
    glColor3f(0.0,0.0,0.0)
    glVertex3f(-0.3,-0.23,-0.23)
    glVertex3f(-0.3,-0.23,0.23)
    glVertex3f(0.3, -0.23, 0.23)
    glVertex3f(0.3,-0.23,-0.23)

    # right side
    glColor3f(0.3,0.3,0.3)
    glVertex3f(-0.3,-0.23,-0.23)
    glVertex3f(-0.25, -0.23, -0.23)
    glVertex3f(-0.05, 0.0, -0.23)
    glVertex3f(-0.1, 0.0, -0.23)

    glVertex3f(-0.1, 0.0, -0.23)
    glVertex3f(-0.1, -0.05, -0.23)
    glVertex3f(0.1, -0.05, -0.23)
    glVertex3f(0.1, 0.0, -0.23)

    glVertex3f(0.1, 0.0, -0.23)
    glVertex3f(0.1, -0.05, -0.23)
    glVertex3f(0.3, -0.23, -0.23)
    glVertex3f(0.35, -0.23, -0.23)

    glVertex3f(-0.2, -0.1, -0.23)
    glVertex3f(-0.2, -0.15, -0.23)
    glVertex3f(0.2, -0.15, -0.23)
    glVertex3f(0.2, -0.1, -0.23)
    # left side
    glColor3f(0.3,0.3,0.3)
    glVertex3f(-0.35,-0.23,0.23)
    glVertex3f(-0.3, -0.23, 0.23)
    glVertex3f(-0.05, 0.0, 0.3)
    glVertex3f(-0.1, 0.0, 0.3)

    glVertex3f(-0.1, 0.0, 0.3)
    glVertex3f(-0.1, -0.05, 0.3)
    glVertex3f(0.1, -0.05, 0.3)
    glVertex3f(0.1, 0.0, 0.3)

    glVertex3f(0.1, 0.0, 0.3)
    glVertex3f(0.1, -0.05, 0.3)
    glVertex3f(0.3, -0.23, 0.23)
    glVertex3f(0.35, -0.23, 0.23)

    glVertex3f(-0.2, -0.1, 0.3)
    glVertex3f(-0.25, -0.15, 0.3)
    glVertex3f(0.2, -0.15, 0.3)
    glVertex3f(0.2, -0.1, 0.3)

    glEnd()


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.0,0.5,1.0,0.0)
    # glPointSize(3.0)

    glPushMatrix()
    glRotatef(20.0, 0.25, 0.15, 0.0)
    ocean()
    glPopMatrix()

    glPushMatrix()
    glRotatef(20.0, 0.25, 0.5, 0.0)
    base()
    glPopMatrix()

    glPushMatrix()
    glRotatef(20.0,0.25,0.5,0.0)
    road()
    glPopMatrix()

    glPushMatrix()
    glRotatef(20.0, 0.25, 0.5, 0.0)
    line()
    glPopMatrix()

    glPushMatrix()
    glRotatef(20.0, 0.25, 0.5, 0.0)
    pillars()
    glPopMatrix()

    glPushMatrix()
    glRotatef(20.0, 0.25, 0.5, 0.0)
    bridge()
    glPopMatrix()

    glFlush()


def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw()
        pygame.display.flip()
        pygame.time.wait(10)

main()