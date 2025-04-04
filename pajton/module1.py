import time
from math import radians, sin,cos,pi
from OpenGL.GL import *
from OpenGL.GLUT import *

w, h = 500,500
current_position = 0
direction = 1
angle = radians(45)

def position():
    global current_position
    global direction
    current_position = direction + current_position
    if current_position > 100:
        direction = -1
    if current_position < 10:
        direction = 1
    return current_position

def circular_motion():
    global angle
    radius = 200
    omega = 0.4
    circlex = 100 + radius + cos(angle)
    circley = 100 - radius + sin(angle)
    angle = angle + omega
    circlex = circlex + radius * omega * cos(angle + pi/2)
    circley = circley - radius * omega * sin(angle + pi/2)
    return circlex, circley

print(circular_motion())
# ---Section 1---
def square():
    newx, newy = circular_motion()
    first_point = 150
    size = 100
    # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    glBegin(GL_QUADS) # Begin the sketch
    glVertex2f(first_point + newx, first_point + newy) # Coordinates for the bottom left point
    glVertex2f(first_point + size + newx, first_point + newy) # Coordinates for the bottom right point
    glVertex2f(first_point + size + newx, first_point + size + newy) # Coordinates for the top right point
    glVertex2f(first_point + newx, first_point + size + newy) # Coordinates for the top left point
    glEnd() # Mark the end of drawing

# This alone isn't enough to draw our square
def iterate():
    glViewport(0, 0, 500,500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

# ---Section 2---

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    glLoadIdentity() # Reset all graphic/shape's position
    iterate()
    glColor3f(1.0, 0.0, 1.0) # Set the color to pink
    square() # Draw a square using our function
    glutSwapBuffers()

#---Section 3---

glutInit()
glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
glutInitWindowSize(500, 500)   # Set the w and h of your window
glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
wind = glutCreateWindow(b"G00wno jebane kurwa mach") # Set a window title
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen) # Keeps the window open
glutMainLoop()  # Keeps the above created window displaying/running in a loop