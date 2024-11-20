import pygame
from pygame.locals import * 
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

display = (1280,720)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("Layered Cubes")

gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0,0,-30)
glScale(2,2,2)

def draw_cube():

# box 
    glBegin(GL_TRIANGLES)
# side 1
    glVertex3f(1,1,1)
    glVertex3f(1,1,-1)
    glVertex3f(1,-1,-1)

    glVertex3f(1,-1,-1)
    glVertex3f(1,-1,1)
    glVertex3f(1,1,1)

# side 2

    glVertex3f(1,1,1)
    glVertex3f(1,1,-1)
    glVertex3f(-1,1,-1)

    glVertex3f(-1,1,-1)
    glVertex3f(-1,1,1)
    glVertex3f(1,1,1)

# side 3
    
    glVertex3f(1,1,1)
    glVertex3f(-1,1,1)
    glVertex3f(-1,-1,1)

    glVertex3f(1,1,1)
    glVertex3f(1,-1,1)
    glVertex3f(-1,-1,1)

# side 4
    
    glVertex3f(-1,-1,-1)
    glVertex3f(1,-1,-1)
    glVertex3f(1,1,-1)

    glVertex3f(-1,-1,-1)
    glVertex3f(-1,1,-1)
    glVertex3f(1,1,-1)

# side 5
    
    glVertex3f(-1,-1,-1)
    glVertex3f(-1,-1,-1)
    glVertex3f(-1,-1,1)

    glVertex3f(-1,1,-1)
    glVertex3f(-1,1,1)
    glVertex3f(-1,-1,1)

# side 6
    
    glVertex3f(-1,-1,-1)
    glVertex3f(1,-1,-1)
    glVertex3f(1,-1,1)

    glVertex3f(-1,-1,-1)
    glVertex3f(-1,-1,1)
    glVertex3f(1,-1,1)

    glEnd()

def draw_object():
    glPushMatrix()
    glScalef(1.2,1.2,1.2)
    glColor3f(0.0, 1.0, 0.0)
    draw_cube()
    glPopMatrix()

    glPushMatrix()
    glScalef(0.9,0.9,0.9)
    glColor3f(0, 0.75, 0)
    draw_cube()
    glPopMatrix()

    glPushMatrix()
    glScalef(0.6,0.6,0.6)
    glColor3f(0,0.50, 0)
    draw_cube()
    glPopMatrix()

    glPushMatrix()
    glScalef(0.3,0.3,0.3)
    glColor3f(0,0.25,0)
    draw_cube()
    glPopMatrix()
    
def controls():
    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_a:
            glTranslatef(-1,0,0)
        if event.key == pygame.K_s:
            glRotatef(45.0, 0.0, 1.0, 0.0)
            glTranslatef(0,-1,0)
        if event.key == pygame.K_d:
            glTranslatef(1,0,0)
        if event.key == pygame.K_w:
            glRotatef(90.0, 0.0, 1.0, 0.0)
            glTranslatef(0,1,0)


while True:
    for event in pygame.event.get():
        controls()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotate(1,1,1,1)
    draw_object()
   
    pygame.display.flip()
    pygame.time.wait(15)
















