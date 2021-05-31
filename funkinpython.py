# from typing import List
from pygameapp import PyGameApp
import pygame.key, pygame.surface, pygame.display, pygame.transform
#from pygame import key
from pygame.locals import *


class Arrow():
    def __init__(self, parent, direction, xposition, key):
        self.parent = parent
        self.direction = direction  #'left', right, up, down
        # self.isPressed = False
        self.defaultImageName = self.direction + "_default.png"
        self.pressedImageName = self.direction + "_pressed.png"
        self.xposition = xposition
        self.defaultImage = None
        self.pressedImage = None
        self.key = key

    def load(self):
        self.defaultImage = pygame.image.load(self.defaultImageName).convert()
        self.pressedImage = pygame.image.load(self.pressedImageName).convert()

    def is_pressed(self):
        # keys = pygame.key.get_pressed()
        if self.parent.keysPressed[self.key]:
            return True
        else:
            return False

    def render(self):

        if self.is_pressed():
            self.parent.surface.blit(self.pressedImage, (self.xposition, 10))
        else:
            self.parent.surface.blit(self.defaultImage, (self.xposition, 10))
            

class Line():
    def __init__(self, parent):
        self.parent = parent
        self.yposition = 300
        self.arrow1image = None

    def load(self):
        self.arrow1image = pygame.image.load("left_default.png").convert()

    def render(self):
        self.parent.surface.blit(self.arrow1image, (10, self.yposition))
        
    def move(self):
        self.yposition -= 1

        if self.parent.keysPressed[K_UP]:
            self.arrow1image = pygame.transform.rotate(self.arrow1image, 180)


class FunkinApp(PyGameApp):
    # variable creation
    def __init__(self):
        super().__init__() 
        self.arrows = []
        self.arrows.append(Arrow(self, 'left', 10, K_LEFT))
        self.arrows.append(Arrow(self, 'left', 100, K_RIGHT))

        self.movingline = Line(self)

        self.width = 800
        self.height = 600
        self.testfont = None
        self.myText = None

    # game load
    def on_start(self):
        self.testfont = pygame.font.SysFont("Verdana", 20)
        self.myText = self.testfont.render( "mart is great", True, (0,0,0))

        for arrow in self.arrows:
            arrow.load()
        self.movingline.load()

    # game logic
    def on_loop(self):
        if self.keysPressed[K_ESCAPE]:
            self.running = False

        self.movingline.move()

    # game display
    def on_render(self):
        #display background
        self.surface.fill((255, 255, 255))
        
        # display arrows
        for arrow in self.arrows:
            arrow.render()

        self.movingline.render()

        self.surface.blit(self.myText, (500,500))
        #diplay notes

if __name__ == "__main__" :

    # myapp = FunkinApp()
    # myapp.start()
    FunkinApp().start()
