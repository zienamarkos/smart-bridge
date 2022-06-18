
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *
import numpy as np
import time
from PIL import Image
from OpenGL.GL.shaders import *


vao, program, texture = None, None, None


def getFileContents(filename):
    p = os.path.join(os.getcwd(), "shaders", filename)
    return open(p, 'r').read()



def init():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-3.0, 3.0, -3.0, 3.0)
    glEnable(GL_DEPTH_TEST)


class Background:
    def __init__(self):
        vertexShader = compileShader(getFileContents(
            "vertex.shader"), GL_VERTEX_SHADER)
        fragmentShader = compileShader(getFileContents(
            "fragment.shader"), GL_FRAGMENT_SHADER)


        self.program = glCreateProgram()
        glAttachShader(self.program, vertexShader)
        glAttachShader(self.program, fragmentShader)
        glLinkProgram(self.program)
        self. vertexes = np.array([
        [10, 1, -.50,    1.0, 0.20, 0.8,    1.0,1.0],
        [1, -1, -.50,   1.0, 1.0, 0.0,     1.0,0.0],
        [-1, 1, -.50,   0.0, 0.7, 0.2,     0.0, 1.0],

        [1, -1, -.50,   1.0, 1.0, 0.0,     1.0,0.0],
        [-1, -1, -.50,  0.0, 0.4, 1.0,     0.0,0.0],
        [-1, 1, -.50,   0.0, 0.7, 0.2,     0.0,1.0],

        ], dtype=np.float32)

        vbo = glGenBuffers(1)

        glBindBuffer(GL_ARRAY_BUFFER, vbo)

        glBufferData(GL_ARRAY_BUFFER, self.vertexes.nbytes, self.vertexes, GL_STATIC_DRAW)

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        glBindVertexArray(vbo)
        glEnableVertexAttribArray(0)
        positionLocation = glGetAttribLocation(self.program, "position")
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE,
                              32, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        colorLocation = glGetAttribLocation(self.program, "color")
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE,
                              32, ctypes.c_void_p(12))
        glEnableVertexAttribArray(1)

        texLocation = glGetAttribLocation(self.program, "texCoord")
        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE,
                             32, ctypes.c_void_p(24))
        glEnableVertexAttribArray(2)

        texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        image = Image.open("images/bg_img.jpg")
        width, height = image.size
        image_data = np.array(list(image.getdata()), dtype=np.uint8)
        bgImg = pygame.image.load('images/bg_img.jpg')
        width,height =  bgImg.get_rect().size
        image_data=pygame.image.tostring(bgImg,'RGBA')
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)
        glGenerateMipmap(GL_TEXTURE_2D)

        glBindTexture(GL_TEXTURE_2D,texture)

        glBindBuffer(GL_ARRAY_BUFFER,0)


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
        
        # pillars
    glBegin(GL_QUADS)

    glColor3f(1,0.5,0.5)
    glVertex3f(-0.35,-0.25,-0.2)
    glVertex3f(-0.31,-0.25,-0.2)
    glVertex3f(-0.31,0.25,-0.2)
    glVertex3f(-0.35,0.25,-0.2)

    glVertex3f(-0.35, -0.25, 0.2)
    glVertex3f(-0.31, -0.25, 0.2)
    glVertex3f(-0.31, 0.25, 0.2)
    glVertex3f(-0.35, 0.25, 0.2)

    glVertex3f(0.35, -0.25, -0.2)
    glVertex3f(0.31, -0.25, -0.2)
    glVertex3f(0.31, 0.25, -0.2)
    glVertex3f(0.35, 0.25, -0.2)

    glVertex3f(0.35, -0.25, 0.2)
    glVertex3f(0.31, -0.25, 0.2)
    glVertex3f(0.31, 0.25, 0.2)
    glVertex3f(0.35, 0.25, 0.2)

    glEnd()


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
    glVertex3f(-0.3,-0.24,-0.23)
    glVertex3f(-0.3,-0.24,0.23)
    glVertex3f(0.3, -0.24, 0.23)
    glVertex3f(0.3,-0.24,-0.23)

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


def translate(y):

    glTranslatef(0.0,y,0.0)
    bridge()

    if  y <= 4.6:
        y += 0.1
    elif y == 4.6:
        y -= 0.1


y_translate = 0.001
start_time=0


def draw():
    global bg
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
    road()
    line()

    global y_translate
    translate(y_translate)
    bridge()
    glPopMatrix()

    end_time = time.time()
    global  start_time
    if end_time - start_time > 15 :
        if y_translate < 0 :
            start_time = time.time()
        y_translate -= 0.001
    else:
        end_time=time.time()
        if end_time-start_time > 5:
            if y_translate < 0.422 :
                y_translate += 0.001

    glFlush()



def main():
    init()
    global bg
    bg = Background()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0.0,0.5,1.0,0.0)
        glBindVertexArray(bg.vao)
        glDrawArrays(GL_TRIANGLES, 0, 6)
        draw()
        pygame.display.flip()
        pygame.time.wait(10)

main()
