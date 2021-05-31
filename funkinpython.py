from typing import List
from pygameapp import PyGameApp
import pygame.key, pygame.surface, pygame.display
#from pygame import key
from pygame.locals import *

class Arrow():
    def __init__(self, direction, xposition, key):
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
        keys = pygame.key.get_pressed()
        if keys[self.key]:
            return True
        else:
            return False

    def render(self, surface):

        if self.is_pressed():
            surface.blit(self.pressedImage, (self.xposition, 10))
        else:
            surface.blit(self.defaultImage, (self.xposition, 10))
            

class ArrowLine():
    def __init__(self):
        self.yposition = 300
        self.arrow1image = None

    def load(self):
        self.arrow1image = pygame.image.load("left_default.png").convert()

    def render(self, surface):
        surface.blit(self.arrow1image, (10, self.yposition))
        
    def move(self):
        self.yposition -= 1

class FunkinApp(PyGameApp):

    def __init__(self):
        super().__init__() 
        self.arrows: List[Arrow] = []
        self.arrows.append(Arrow('left', 10, K_LEFT))
        self.arrows.append(Arrow('left', 100, K_RIGHT))

        self.line = ArrowLine()

        self.width = 800
        self.height = 600

    def on_start(self):
        for arrow in self.arrows:
            arrow.load()
        self.line.load()

    def on_loop(self):
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            self.running = False

        self.line.move()

    def on_render(self):
        #display background
        self.surface.fill((255, 255, 255))
        
        # display arrows
        for arrow in self.arrows:
            arrow.render(self.surface)

        
        self.line.render(self.surface)
        #diplay notes

if __name__ == "__main__" :

    # myapp = FunkinApp()
    # myapp.start()
    FunkinApp().start()
